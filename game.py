import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack',
         '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'ace', 'king', 'queen', 'jack']

ace = 1
king = 10
queen = 10
jack = 10


def user_turn():
    """
    A short function which randomises the cards and gives one to the user
    """
    print("Your Turn:")
    randomised = random.choice(cards)
    print(randomised)
    return randomised


def user():
    """
    This will give the user and the opponent their first card
    and will give the user the chance to get another card or
    stay with what they have.
    """
    user_total = 0
    user_result_one = user_turn()

    while True:
        intro = input("Hit or Stick:\n")

        print("Opponents Turn...\n")
        randomised_two = random.choice(cards)
        print(randomised_two)
        opponent_score = randomised_two
        

        if intro.lower().strip().endswith('hit'):
            user_result_two = user_turn()
            user_total += value(user_result_two)

            if user_total > 21:
                print("You've lost, better luck next time!")
                return user_total

        elif intro.lower().strip().endswith('stick'):
            # print("Opponents Turn...\n")
            randomised_two = random.choice(cards)
            # print(randomised_two)

        else:
            print("Invalid input. Please enter 'Hit' or 'Stick'.")

    return user_total


def value(card):
    """
    Gives value to ace cards
    """
    if card.isdigit():
        return int(card)
    elif card.lower() == 'ace':
        return ace
    else:
        return 10

# def opponent():
    """
    The score for the opponent which will be automised.
    """
    # print("Opponents Turn...\n")
    # randomised_two = random.choice(cards)
    # print(randomised_two)


def main():
    """
    Adds all the function in to one to increase efficiency.
    """
    # opponent()
    user_score = user()
    print(f"User's Total Score: {user_score}")


def menu():
    """
    A menu that will show the user a variety of choices
    """
    print("[1] Play The Game!")
    print("[2] How to Play")
    print("[3] Credits")
    print("[0] Exit the programn.")


menu()
answer = int(input("Enter your option: "))

while answer != 0:
    if answer == 1:
        print("Option 1 has been chosen.")
        main()
    elif answer == 2:
        print("Option 2 has been chosen.")
        print("Welcome to a game of 21, you will")
        print("have to get the closest to 21 as possible\n")
        print("Your opponent is also trying to get as close to 21 but if")
        print("they reach 17 or higher they can not get another card.\n")
    elif answer == 3:
        print("Option 3 has been chosen.")
        print("https://github.com/oscarbutler")
    else:
        print("Invalid Option.")

    menu()
    print()
    answer = int(input("Enter your option: "))
