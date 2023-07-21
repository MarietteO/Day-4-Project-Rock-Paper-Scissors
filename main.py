import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def choose_art(choice):
    """Displays the corresponding art for the given choice."""
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)

computer_wins = [(0, 1), (1, 2), (2, 0)]
user_wins = [(0, 2), (1, 0), (2, 1)]
draw = [(0, 0), (1, 1), (2, 2)]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0, 2)
combination = (user_choice, computer_choice)

choose_art(user_choice)
print("The computer chose:")
choose_art(computer_choice)
if combination in computer_wins:
    print("Computer wins")
elif combination in user_wins:
    print("You win")
else:
    print("It's a draw")



