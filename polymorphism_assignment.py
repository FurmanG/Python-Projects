"""
POLYMORPHISM SUBMISSION ASSIGNMENT - Step: 245
Create two classes that inherit from another class.
1.  Each child should have at least two of their own attributes.
2. The parent class should have at least one method (function).
3. Both child classes should utilize polymorphism on the parent class method.
4. Add comments throughout your Python explaining your code.
May 12 2022
Gil Furman
"""

# parent class
class vehicle:
  def __init__(self, engine, number_of_doors, number_of_seats,max_speed):
    self.engine = engine
    self.number_of_doors = number_of_doors
    self.number_of_seats = number_of_seats
    self.max_speed = max_speed
  def moving(self):
    print("I can move at a speed of {}\n".format(self.max_speed))      


# child class 
class tractor(vehicle):
  horsepower = ""
  for_agricultur = False
  # polymorphism on the parent class method
  def moving(self):
    print("I can plow at {} horsepower\n".format(self.horsepower))

# child class
class helicopter(vehicle):
  max_height_reached = ""
  max_range = ""
  # polymorphism on the parent class method
  def moving(self):
    print("I can fly at a speed of {}, \nat a maximun altitude of {} \n, to a range of {} \n".format(self.max_speed, self.max_height_reached, self.max_range))


if __name__ == "__main__":

  John_Deere_8630H = tractor("Reman", "2", "1", "50")
  John_Deere_8630H.horsepower = "672"
  John_Deere_8630H.for_agricultur = True
  print(John_Deere_8630H.for_agricultur)
  John_Deere_8630H.moving()

  Sikorsky_H92 = helicopter("CT7-8A", "4", "24", "190")
  Sikorsky_H92.max_height_reached = "20,000 ft"
  Sikorsky_H92.max_range = "1000 km"
  Sikorsky_H92.moving()


  Bus = vehicle("L9N", "2", "51","80")
  Bus.moving()
