"""
  Build three classes, two of which must inherit from the first and employ
  polymorphism. Between the three classes, there must be at least 5 methods,
  3 instance attributes, 1 class attribute, and the parent class should
  have a dunder init. If you want you can add dunder str and dunder repr 
  to each class.
"""
class Member:
  def __init__(self, char_name, level, char_class, guild='Omen'):
    self.char_name = char_name
    self.level = level
    self.char_class = char_class
    self.guild = guild
  def rank(self):
    print("I am here to server")
    

class Officer(Member):
  def rank(self):
    print("I am here to lead")

class Leader(Officer, Member):
  def rank(self):
    print("Serve me well")


