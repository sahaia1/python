import random


class Node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def set_left(self, left):
    self.left = left

  def set_right(self, right):
    self.right = right

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  def get_data(self):
    return self.data

  def debug_left(self):
    return self.left is None

  def debug_right(self):
    return self.right is None


class BST(object):
  def __init__(self):
    self.head = None
    self.size = 0

  def insert(self, data):
    print "inserting data - {}".format(data)
    new_node = Node(data)
    if not self.head:
      self.head = new_node
    else:
      current = self.head
      prev = None
      while current:
        prev = current
        if current.get_data() > new_node.get_data():
          current = current.get_left()
        else:
          current = current.get_right()
      if new_node.get_data() < prev.get_data():
        prev.set_left(new_node)
      else:
        prev.set_right(new_node)

  def print_tree(self, pointer=-5, d=0, path=0):
    if pointer == -5:
      pointer = self.head
    if pointer:
      print 2 * d * " " + str(path) + "." + str(pointer.get_data())
      self.print_tree(pointer.get_left(), d + 1, path+1)
      self.print_tree(pointer.get_right(), d + 1, path+1)

  def debug(self):
    print self.head.debug_left()
    print self.head.debug_right()


if __name__ == '__main__':
  tree = BST()
  for _ in range(20):
    tree.insert(random.randint(100, 200))

  tree.print_tree()




