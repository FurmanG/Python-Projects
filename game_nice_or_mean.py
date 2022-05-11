#
#
# Python: 3.10.4
#
# Author: Daniel A. Christie
#
# Purpose: The Tech Academy - Python Course, Drill
#
#
import winsound # import windsound module for Windows Platform only. 


from dataclasses import dataclass

###### statr function ######
def start(nice=0,mean=0,name=""):
  # get user's name
  name = describe_game(name)
  nice,mean,name = nice_mean(nice,mean,name)

###### describe_game function ######
def describe_game(name):
  """ check if this is a new game or not. if it is new, get the user's name.
    If it is not a new game, thank the player for playing again and continue with the game """
  if name != "":
    print("\nThank you for playing again, {}!".format(name))
  else:
    stop = True
    while stop:
      if name == "":
        name = input("\nWhat is your name? \n>>> ").capitalize()
        if name !="":
          print("\nWelcome, {}!".format(name))
          print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
          print("but at the end of the game your fate \nwill be sealed by your actions.")
          stop = False
  return name

###### nice_mean function ######
def nice_mean(nice, mean, name):
  stop = True
  while stop:
    show_score(nice,mean,name)
    pick = input("\nA stranger approched you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>:").lower()
    if pick == "n":
      print("\nthe stranger walks away smiling...")
      nice = (nice + 1)
      stop = False
    if pick == "m":
      print("\nThe stranger glares at you \nmenacingly and storms off....")
      mean = (mean + 1)
      stop = False
  score(nice,mean,name) # pass the 3 variables to the score() 

###### show_score function ######
def show_score(nice,mean,name):
  print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

###### score function ######
def score(nice,mean,name):
  # score function is being passed the values stored within the 3 variables 
  if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
    win(nice,mean,name)
  if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
    lose(nice,mean,name)
  else: # else, call nice_mean function passing in the variables so it can use them
    nice_mean(nice,mean,name)

###### win function ######
def win(nice,mean,name):
  #Substitute the {} wildcards with our variable values
  print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
  # playing music for the winner, AFTER the music segment ended the game continues ... and asks "Do you want to play again?"
  winsound.PlaySound("star-wars-theme.wav",winsound.SND_FILENAME)
  # Call again function and pass in our variables 
  again(nice,mean,name)

###### lose function ######
def lose(nice,mean,name):
  # Substitute the {} wildcards with our variable values
  print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
  #playing music for the winner, AFTER the music segment ended the game continues ... and asks "Do you want to play again?"
  winsound.PlaySound("good-bad-ugly.wav",winsound.SND_FILENAME)
  # call again function and pass in our variables
  again(nice,mean,name)

###### again function ######
def again(nice,mean,name):
  stop = True
  while stop:
    choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
    if choice == "y":
      stop = False
      reset(nice,mean,name)
    if choice == "n":
      print("\nOh, so sad, sorry to see you go!")
      stop = False
      quit()
    else:
      print("\nEnter ( y ) for 'YES', ( N ) for 'NO':\n>>> ")


  
###### reset function ######
def reset(nice,mean,name):
  nice = 0
  mean = 0
  # Notice, I do not reset the name variable as that same user has elected to play again
  start(nice,mean,name)



if __name__ == "__main__":
  start()