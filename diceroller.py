import random 
def roll_dice():
    dice = random.randint(1, 6)  # pick number between 1-6
    print(f"\n🎲 You rolled a {dice}!")

while True:
    input("\nPress Enter to roll the dice or type 'q' and hit Enter to quit: ")
    user_input = input("Roll again? (Press Enter or type 'q' to quit): ").lower()
    if user_input == 'q':
        print("👋 Exiting Dice Roller. Goodbye!")
        break
    roll_dice()