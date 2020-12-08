class Example:
  "A basic example class that returns a function object"
  def b(self):
    return "this is an example class"

c = Example()


class Square:
   def __init__(self, length, width):
       self.length = length
       self.width = width
   def area(self):
       return self.width * self.length
r = Square(20, 2000)
print("Rectangle Area: %d" % (r.area()))


class PartsColor:
  "Creates a class"
  def __init__(self):
    "Create a new color for each part"
    self.hood = "Blue"
    self.wheels = "Red"
    self.doors = "Green"
e = PartsColor() # Instantiate two objects to represent points
f = PartsColor()

print(e.hood, f.wheels, e.hood, f.wheels, e.doors, f.doors)  # Assign each point a unique location