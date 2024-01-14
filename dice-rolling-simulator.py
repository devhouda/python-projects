import random

def roll_dice():
    return random.randint(0,6)

dice_drawings = {
    1: """
       ┌───┐
       │   │
       │ ● │
       │   │
       └───┘
    """,
    2: """
       ┌───┐
       │ ● │
       │   │
       │ ● │
       └───┘
    """,
    3: """
       ┌───┐
       │ ● │
       │ ● │
       │ ● │
       └───┘
    """,
    4: """
       ┌─────┐
       │ ●  ●│
       │ ●  ●│
       └─────┘
    """,
    5: """
       ┌─────────┐
       │ ●     ● │
       │    ●    │
       │ ●     ● │
       └─────────┘
    """,
    6: """
       ┌──────┐
       │ ●  ● │
       │ ●  ● │
       │ ●  ● │
       └──────┘
    """
}


while True:
    roll_y_n = input("Roll the dice? (y/n) ")
    if roll_y_n.lower() == "y".lower():
        dice1 = roll_dice()
        dice2 = roll_dice()
        print(f"dice rolled: {dice1} and {dice2}")
        print(f"{dice_drawings[dice1]} '\t' {dice_drawings[dice2]}")
    elif roll_y_n.lower() == "n".lower():
        print("Program ended.")
        quit()
    else:
        print("Invalid input, please enter y for yes or n for no!")

