""" 
INHERITANCE SUBMISSION ASSIGNMENT
Create two classes that inherit from another class.
1. Ensure each child has at least two of their own attributes.
2. Add comments throughout your Python explaining your code. 
"""
# parent class
class animal:
  def __init__(self, name, age, animal_type, food_type):
    self.name = name
    self.age = age
    self.animal_type = animal_type
    self.food_type = food_type
  def eat(self):
    print("{} eats now".format(self.name))      
  def sleep(self):
    print("{} is sleeping now".format(self.name))

# child class
class dog(animal):
  breed = ""
  running_speed = ""
  def barking(self):
    print("{} is barking now".format(self.name))

# child class
class parrot(animal):
  language = ""
  living_range =""
  def speaking(self):
    print("{} is speaking now".format(self.name))


# object initialization
dog_1 = dog("Rocky", "4", "Dog", "Bonzo")   
parrot_1 = parrot("Frank", "2", "Parrot", "Seeds") 

dog_1.breed = "Beagle"
dog_1.running_speed = "20mph"

parrot_1.language = "Turkish"
parrot_1.living_range = "Turkey"

print("{} live in {} and speak {} ".format(parrot_1.name, parrot_1.living_range, parrot_1.language))
parrot_1.speaking()

print("{} is a {} and he runs at a speed of {}".format(dog_1.name, dog_1.breed, dog_1.running_speed))
dog_1.barking()