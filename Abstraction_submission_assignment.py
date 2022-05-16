"""
ABSTRACTION SUBMISSION ASSIGNMENT.

Gil Furman
May 16 2022
"""

from abc import ABC, abstractmethod
from ast import Pass

class Vehicl(ABC): # A class that utilizes the concept of abstraction
  @abstractmethod  
  def go(self):  # An abstract method
    pass 

  def stop(self): # A regular method
    print("You stopped")

class Car(Vehicl): # A child class of Vehicl
  def go(self): # A method that override the abstract parent method.
    print("You drive the car")

if __name__ == "__main__":
  BMW = Car() # An object that utilizes both the parent and child methods.
  BMW.go() # The object utilizes the child methods.
  BMW.stop() # The object utilizes the parent methods.

