from random import randint
#import turtle #later
import draw

print("Lets Play Hangman!")  #gameplan from notes.txt, wordpad
#draw.hello()
#hangman = [
#draw.head(),draw.body(), draw.arms(1),draw.arms(2)

words = ["codefu", "code", "awesome", "stars", "skeleton", "pumpkin"]

random = randint(0, len(words) - 1)
current = words[random]
tries = 6  #for test. Each limb on a hangman

#draw.hangman(tries-1)

guesses = ""  #we're gonna add each letter to the string, it'll be like a list but easier

#SKIP TURTLE
#import turtle at top now
#screen = turtle.Screen().bgcolor("light blue") #comment it out

#Set up end while else first before draw function, leave space for d funct


#briefly explain functions
def draw_word():  #draws and updates the blanks
  word_draw = ""  #show two.py example

  for letter in current:
    if letter in guesses:
      word_draw = word_draw + letter
    else:
      word_draw = word_draw + "_"
    word_draw = word_draw + " "

  print(word_draw)
  #draw.hangman(tries)

  if "_" not in word_draw:
    print("You Win!")
    exit(0)
  else:
    print("You have ", tries, " tries left.")
    draw.hangman(tries)
    print("Please guess a letter:")


#set up the while else first, its like if/else
while tries > 0:
  draw_word()
  player = input()[0]
  guesses += player
  #means guesses = guesses + player, shortcut

  if player not in current:
    print("\n>Try Again!")
    tries = tries - 1
#must change tries to 6
#draw.hangman(tries)
  else:
    print("\n>Right!")
else:
    draw.hangman(tries)
    print("Game Over! The word was:", current)
