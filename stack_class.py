import random


class Node(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def set_next(self, next):
    self.next = next

  def get_next(self):
    return self.next

  def get_data(self):
    return self.data


class Stack(object):
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, data):
    new_node = Node(data)
    self.size += 1
    if not self.head:
      self.head = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node

  def pop(self):
    if not self.head:
      print "List is empty"
      return -1
    else:
      self.size -= 1
      value = self.head.get_data()
      self.head = self.head.get_next()
      return value

  def is_empty(self):
    return self.size == 0

  def size(self):
    return self.size

  def peek(self):
    if not self.head:
      return -1
    return self.head.get_data()

  def print_stack(self):
    if not self.head:
      print 'List is empty'
      return
    else:
      pointer = self.head
      while pointer:
        print "{}\t".format(pointer.data),
        pointer = pointer.get_next()
      print "\n"


if __name__ == "__main__":
  s = Stack()
  for _ in range(20):
    s.push(random.randint(1, 100))
  s.print_stack()
  t = Stack()
  for _ in range(12):
    t.push(random.randint(300, 400))
  t.print_stack()

  new_stack = Stack()
  while not s.is_empty() and not t.is_empty():
    new_stack.push(s.pop())
    new_stack.push(t.pop())

  if s.is_empty():
    while not t.is_empty():
      new_stack.push(t.pop())
  else:
    while not s.is_empty():
      new_stack.push(s.pop())

  new_stack.print_stack()
