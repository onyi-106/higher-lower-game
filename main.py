import random
import art
from game_data import data
from replit import clear


#Write a code that choose a random item inside the data dictionary and then store inside a variable
# print(art.logo)
game_over = False
score = 0
#Generate random data
def data_gen():
  return random.choice(data)
############################

a = random.choice(data)
b = random.choice(data)

#Functions to access item inside dictionary
def name(a_or_b):
  return a_or_b["name"]
def followers(a_or_b):
  return a_or_b["follower_count"]
def desc(a_or_b):
  return a_or_b["description"]
def country(a_or_b):
  return a_or_b["country"]
##############################################
  
is_over = False
while not is_over:
  #Debugger
  # print(f"{a}\n{b}")
  ####################
  compare_a = f"Compare A: {name(a)}, a {desc(a)}, from {country(a)}."
  print(compare_a)
  print(art.vs)
  compare_b = f"Against B: {name(b)}, a {desc(b)}, from {country(b)}."
  print(compare_b)
  
  compare = input("Who has more followers? Type 'A' or 'B': ").lower()
  if compare == "b":
    if followers(b) > followers(a):
      score += 1
      a = b
      b = data_gen()
      #If after generating a data, the data 'a' is the same as the data 'b', then generate again
      while a == b:
        b = data_gen()
      clear()
      print(f"You're right! current score: {score}.")
    else:
      is_over = True
      clear()
      print(f"Sorry thats wrong. Your final score: {score}")
      
  elif compare == "a":
    if followers(a) > followers(b):
      score += 1
      a = b
      b = data_gen()
      #If after generating a data, the data 'a' is the same as the data 'b', then generate again
      while a == b:
        b = data_gen()
      clear()
      print(f"You're right! current score: {score}.")
    else:
      is_over = True
      clear()
      print(f"Sorry thats wrong. Your final score: {score}")
  #If player choose neither a or b:
  else:
    is_over = True
    clear()
    print(f"Sorry thats wrong. Your final score: {score}")