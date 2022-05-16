"""
ENCAPSULATION SUBMISSION ASSIGNMENT
Gil Furman
May 16 2022
"""
# ===================protected======================
# Class with variables and method that are protected
# That mean, "don't use these unless you really know you should."
# This is just a convention, it doesn't change how the method can be accessed.
class Car_protected():
  def __init__(self,doors,enginetype):
    self._doors=doors # Protected variable
    self._enginetype=enginetype # Protected variable
  def _data_print(self): # Protected method
    print("This method is protected") 

BMW = Car_protected(4,"V8")
print("The number of doors in this BMW is {}. ".format(BMW._doors))
BMW._doors = 2 # We can change the doors number, but we need to avoid it.
print("The number of doors in this BMW is {}. ".format(BMW._doors))
BMW._data_print() # We can use a protected method like that, but we need to avoid it.

# ===================private======================
# Class with variables and method that are private
class Car_private():
  def __init__(self,doors,enginetype):
    self.__doors=doors # Private variable
    self.__enginetype=enginetype # Private variable

  def set_doors(self,w): 
    self.__doors=w

  def get_doors(self):
    return self.__doors
    
  def __data_print(self): # Private method
    print("This method is private, it can be access with \" object._class__method\" but we need to avoid it")  


if __name__ == "__main__":
  Fiat = Car_private(4,"V2")
  print("The number of doors in this Fiat is {}. ".format(Fiat.get_doors())) # we use the get_doors() method to get the doors number
  Fiat.set_doors(2) # we use the set_doors() method to access the doors number
  print("The number of doors in this Fiat is {}. ".format(Fiat.get_doors()))
  Fiat._Car_private__data_print() # We can use a private method like that, but we need to avoid it. 

