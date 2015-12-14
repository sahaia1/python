import threading
from Queue import Queue, Empty
from time import sleep


class Read(threading.Thread):
  def __init__(self, queue, filename, event):
    super(Read, self).__init__()
    self.filename = filename
    self.queue = queue
    self.event = event

  def run(self):
    self.event.set()
    fd = open(self.filename, 'r')
    for line in fd.readlines():
      # print line
      self.queue.put(line)
    fd.close()

class Write(threading.Thread):
  def __init__(self, queue, filename, event):
    super(Write, self).__init__()
    self.queue = queue
    self.filename = filename
    self.event = event


  def run(self):
    fd = open(self.filename, "w")
    while True and self.event.is_set():
      try:
        text = self.queue.get_nowait()
        alpha = text.split("\t")[0]
        fd.write(alpha + "\n")
      except Empty:
        pass
    fd.close()
    print "Write thread exiting\n"

class Write2(threading.Thread):
  def __init__(self, queue, filename, event):
    super(Write2, self).__init__()
    self.queue = queue
    self.filename = filename
    self.event = event


  def run(self):
    fd = open(self.filename, "w")
    while True and self.event.is_set():
      try:
        text = self.queue.get(block=False)
        num = text.split("\t")[1].strip()
        fd.write(num + "\n")
      except Empty:
        pass
    fd.close()
    print "Write2 thread exiting\n"


if __name__ == "__main__":
  event = threading.Event()
  queue = Queue()


  read_thread = Read(queue, "abc.txt", event)
  read_thread.start()
  write_thread1 = Write(queue, "write1.txt", event)
  write_thread2 = Write2(queue, "write2.txt", event)
  write_thread1.start()
  write_thread2.start()

  read_thread.join()
  sleep(1)
  event.clear()
  write_thread2.join()
  write_thread1.join()
  print queue.qsize()


