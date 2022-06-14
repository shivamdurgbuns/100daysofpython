class Rectangle:
  '''
  This is a rectangle class which will create a rectangle and its properties
  '''

  def __init__(self, width, height):

    self.widht = width
    self.height = height

  def set_width(self, width):
    self.widht = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.widht * self.height)

  def get_perimeter(self):
    return (2*(self.widht+self.height))

  def get_diagonal(self):
    return ((self.widht ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.widht >= 50 or self.height >= 50:
      return "Too big for picture."
    
    pic = ['*'*self.widht for i in range(self.height)]
    return '\n'.join(pic)+'\n'

  def get_amount_inside(self, shape):
    return self.get_area()//shape.get_area()

  def __str__(self):
      return f"Rectangle(width={self.widht}, height={self.height})"

class Square(Rectangle):
  
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def set_side(self, side):
    self.widht = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.widht})"