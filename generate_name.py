import random

# Expanded and diverse lists of names
first_names = ["Ava", "Ethan", "Sophia", "Liam", "Maya", "Elijah", "Olivia", "Noah"]
last_names = ["Harper", "Anderson", "Blake", "Carter", "Diaz", "Evans", "Foster", "Griffin"]

def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

def main():
    print("Welcome to The Sims-inspired Name Generator!")
    while True:
        print("\nGenerated Name:")
        print(generate_name())
        choice = input("Press 'r' to roll again, 'q' to quit: ").lower()
        if choice == 'q':
            print("Thanks for playing! Happy name creating!")
            break

main()
