class Node(object):
  def __init__(self, data, right, left):
    self.data = data
    self.right = right
    self.left = left
    self.parent = None

  def set_left(self, left):
    self.left = left

  def set_right(self, right):
    self.right = right

  def set_parent(self, parent):
    self.parent = parent

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  def get_parent(self):
    return self.parent

  def is_leaf(self):
    return self.right is None and self.left is None


def add_node(data, head):
  new_node = Node(data)
  if not head:
    head = new_node
  else:
    current = head
    while True:
      left = current.get_left()
      if left:
        right = current.get_right()
      if right:


