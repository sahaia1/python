class Test(object):
    def __init__(self, *options, **vals):
        self.options = options
        self.vals = vals

    def display(self):
        print type(self.options)
        for each in self.options:
          print each

    def display_vals(self):
      print type(self.vals)
      for each in self.vals.keys():
        print self.vals[each]


class Test2(object):
    def __init__(self, *options):
        self.options = options
        self.vals = vals

    def display(self):
        print type(self.options)
        for each in self.options:
          print each

    def display_vals(self):
      print type(self.vals)
      for each in self.vals.keys():
        print self.vals[each]



if __name__ == "__main__":
    objs = Test2("aditya", "sahai", 1, 3.56, ["what", "the", "hell"], ("tup1", "tup2"), value1=1, value2=2)
    objs.display()
    objs.display_vals()
