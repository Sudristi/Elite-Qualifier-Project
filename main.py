import random
import sys
print("Hello, Welcome!")
print()
name = input('What is your name?\n')
answer=input(f'\nHow was your day {name}?\n')
def bot_answers(input):
 answers_choices = [
  f"That's Nice! {name}",
  f"Wow! That's great {name}!",
  'Amazing!',
  'Really!'
]
 return random.choice(answers_choices)

while answer != "q":
  answer = input(bot_answers(answer)+"\n")
sys.exit("Program quit")