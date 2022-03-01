import random
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
user_choice = user_input

ascii_art = [rock, paper, scissors]

# User's Choice Info
print("Your Choose:")
print(ascii_art[user_choice])

# Computer's Choice Info
print("Computer Choose:")
print(ascii_art[computer_choice])

if computer_choice == 0 and user_choice == 1:
    print("You Won ✌️✌️✌️.")
elif computer_choice == 1 and user_choice == 2:
    print("You Won ✌️✌️✌️ .")
elif computer_choice == 2 and user_choice == 0:
    print("You Won ✌️✌️✌️.")
elif computer_choice == 1 and user_choice == 0:
    print("You Lose 😢😢😢.")
elif computer_choice == 2 and user_choice == 1:
    print("You Lose 😢😢😢.")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose 😢😢😢.")
else:
    print("Game Draw 🤝🤝🤝.")
