import random


print("Welcome to a game of 21, you will")
print("have to get the closest to 21 as possible\n")
print("Your opponent is also trying to get as close to 21 but if")
print("they reach 17 or higher they can not get another card.\n")

cards = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack']

ace = 1 or 10
king = 10
queen = 10
jack = 10

print("Your Turn:")
randomised = random.choice(cards)
user_result_one = print(randomised)
randomised_two = random.choice(cards)


def user():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """
    global user_total
    user_total = [user_result_one]
    intro = input("Hit or Stick:\n")
    if intro.lower().strip().endswith('Hit'):
        user_result_one
    if intro.lower().strip().endswith("Stick"):
        print("Opponents Turn...\n")
    # if user_total > 21:
    #   print("You've lost, better luck next time!")
    #  return
    if intro.endswith('Hit'):
        print(user_result_two)
    else:
        print("Invalid input. Please enter 'Hit' or 'Stick'.")
        user()

# def second_turn():
    # if intro.endswith('Hit'):
    # print(user_result_two)


def opponent():
    """
    The score for the opponent which will be automised.
    """
    print("Opponents Turn...\n")
    print(randomised_two)


def main():
    """
    Adds all the function in to one to increase efficiency.
    """
    opponent_score = opponent()
    user_score = user()


main()

def menu():