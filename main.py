import random
print("Hello, Welcome!")
print()
name = input('What is your name?\n')
def bot_answers(input):
 answers_choices = [
  f"That's Nice! {name}",
  f"Wow! That's great {name}!",
  'Amazing!',
  'Really!'
]
 return random.choice(answers_choices)
  
quit_letter = 'q'

answer=input(f'\nHow was your day {name}?\n')

while answer != quit_letter:
   answer = input(bot_answers(answer)+"\n")
print("Have a great rest of your day!")
