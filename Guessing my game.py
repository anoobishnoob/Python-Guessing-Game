#lo-hi game
# games details 
# you have to have a random number generator probably some kind of function called Random
# you have to guess a random number from 1-10
# you get 3 guesses
# if guess is too low it should print "too low"
# if guess is too high it should print "too high"
# if you get the number right it prints "you win"
# if you get it wrong after 3 guesses then "you lose"
'''
import random 
import math
random = random.random()
x = math.floor(10*random.random()) + 1
'''
# this is the random number generator code that was given in class
import random 
import math
rand = random.random()
rand = math.floor(10*random.random()) + 1


# rules for the user

print("""The computer has created a random integer from 1-10 for you to guess.\nif you get the answer right then it will print some winning message \nyou have three guesses to get this right. \nIf the answer is too high then this shall say "too high!",\nand if the answer is too low the computer will say "too low!"\nif you do not get the integer correct then you lose.""")
# I used triple quotation marks just because I used quotation marks in my print statement, and did not want to have to reformat stuff. 
# this makes everything look in my opinion just look nicer to the end user

print("\nPlease make your first guess.")
#print ("The random number is",rand) # this line is for testing purposes
guess = float(input()) # first guess
if guess == rand: 
  print("you got the correct answer on your first try!") # I made it give a different message for winning on first try. 
  
elif guess > rand: # first branch of logic 
  print("too high!\nGuess again")
  
  guess = float(input()) # second guess
  if guess == rand: 
    print("You win!")
    
  elif guess > rand: 
    print("too high!\nGuess again")
    
    guess = float(input())# third guess
    if guess == rand:
      print("you win!")
      
    else:
      print("you lose.")
    
  elif guess < rand: 
    print("too low!\nGuess again")
    
    guess = float(input()) # third guess
    if guess == rand:
      print("you win!")
      
    else:
      print("you lose.")
    
elif guess < rand:  # second branch of logic
  print("too low!\nGuess again")
  
  guess = float(input()) # second guess
  if guess == rand: 
    print("You win!")
    
  elif guess > rand: 
    print("too high!\nGuess again")
    
    guess = float(input())# third guess
    if guess == rand:
      print("you win!")
      
    else:
      print("you lose.")
  
  elif guess < rand: 
    print("too low!\nGuess again")
    
    guess = float(input()) # third guess
    if guess == rand:
      print("you win!")
      
    else:
      print("you lose.")

else:
  print("uhm what")
  #just threw this in at the end for fun 
  
  '''
  So just some background for this code
  since I don't think I am allowed to use a while loop for this I decided to just basically use a flow chart kind of method.
  in this code specifically the amount of branch of this tree kind of double every branch
  if you get it right then it just exits the code 
  if you get too high or too low, it brings you to a branch of code that will evalute a guess again 
  the last if statement does not need a elif statement because I want to end the game after all of this. 
  so if you do not get the answer it just ends the game with a lose statement.
'''
