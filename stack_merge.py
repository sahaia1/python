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


def push(data, head):
  if not head:
    head = Node(data)
    return head
  else:
    newNode = Node(data)
    newNode.set_next(head)
    head = newNode
    return head


def insert_at_end(head, data):
  if not head:
    print 'List is empty'
    return
  else:
    current = head
    while current.get_next():
      current = current.get_next()
    new_node = Node(data)
    current.set_next(new_node)


def insert(head, pos, data):
  print "insert: pos - {} - data - {}".format(pos, data)
  if not head:
    print "List is empty"
    return
  else:
    if pos == 0:
      
    current = head
    for _ in range(pos - 1):
      current = current.get_next()
      if not current:
        print "List end reached"
        return
    newNode = Node(data)
    newNode.set_next(current.get_next())
    current.set_next(newNode)


def print_list(head):
  if not head:
    print 'List is empty'
    return
  else:
    current = head
    while current:
      print "\t{}".format(current.get_data()),
      current = current.get_next()
  print "\n"


def alternate_merge(head1, head2):
  current1 = head1
  current2 = head2
  i = 1
  while current1 and current2:
    insert(head1, i, current2.get_data())
    i += 2
    current2 = current2.get_next()
    current1 = current1.get_next()
  # if not current1:
  return head1

if __name__ == "__main__":
  head1 = None
  for _ in range(10):
    head1 = push(random.randint(1, 100), head1)
  print_list(head1)
  insert_at_end(head1, random.randint(500, 600))
  print_list(head1)
  insert(head1, random.randint(0, 9), random.randint(200, 300))
  print_list(head1)

  head2 = None
  for _ in range(12):
    head2 = push(random.randint(1, 100), head2)
  print_list(head2)

  alternate_merge(head1, head2)
  print_list(head1)

