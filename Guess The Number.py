#Guess the Number Game!!

#Library Includes
import random

#Global Definitions
LOW_BOUND = 1
HIGH_BOUND = 20
MAX_NUM_OF_TURNS = 5
reset = "Yes"

#Main program body
name = raw_input("Hello! What is your name?\n")
while (reset == "Yes") or (reset == "yes") or (reset == "YES") or (reset == "y"):

   print "Well, %s, I'm thinking of a number between %s and %s" % (name, str(LOW_BOUND), str(HIGH_BOUND))
   print "Take a guess. Be aware you have only %s guesses" %MAX_NUM_OF_TURNS

   random_number = random.randint(LOW_BOUND, HIGH_BOUND)

   for guess_count in range(1, MAX_NUM_OF_TURNS+1):

      guessed_number = int(raw_input())
      
      if (guessed_number == random_number):
         print "Good job, %s, You guessed my number in %s guesses" % (name, str(guess_count))
         break
      elif (guessed_number > random_number):
         print "Your guess is too high"
         if guess_count >= MAX_NUM_OF_TURNS:
            print "Sorry you couldn't guess the number in %s turns, GAME OVER!" %MAX_NUM_OF_TURNS
      elif (guessed_number < random_number):
         print "Your guess is too low"
         if guess_count >= MAX_NUM_OF_TURNS:
            print "Sorry you couldn't guess the number in %s turns, GAME OVER!" %MAX_NUM_OF_TURNS
      else:
         print "Invalid input"
         break

   reset = raw_input("Do you want to play again? Yes/No")

print "Thank you for playing Guess the Number game"
