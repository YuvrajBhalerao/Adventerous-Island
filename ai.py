import random

def random_event():
    events = [
        "You found a treasure chest!", 
        "You meet a friendly traveler who gives you supplies. She is so beautiful such that you lost your conciousness", 
        "You fall into a hidden trap and lose some health.", 
        "You discover a magical fountain that restores your health.", 
        "A storm forces you to take shelter and lose time.",
        "You find a mysterious map leading to unknown riches."
    ]
    return random.choice(events)

def wild_animal_event():
    animal_name = "A Gujarati Dog"
    description = "Throw a Dhokla, Fafda or a Thepla towards him and he won't harm you."
    print(f"\nA wild animal attacks! It's {animal_name}!")
    print(f"Description: {description}\n")
    action = input("Do you want to (1) Throw food or (2) Run away? Enter your choice: ")
    if action == "1":
        print(f"You threw some food. {animal_name} is happy and leaves you unharmed.")
        print("Gujarati Dog: \"Tamémàrà dhokla bahu saara chhe. Tamaro Aabhar!\" (Your dhokla is delicious. Thank you!)\n")
    else:
        print("You tried to run away but got slightly injured.")
        return random.randint(10, 20)  # Damage taken when running away
    return 0

def main():
    print("Welcome to the most Adventureous Game ever created on this planet!")
    print("In this game, you are an adventurous explorer venturing into a mysterious and unpredictable land. Your goal is to survive, collect treasures, and uncover hidden secrets.")
    print("Be prepared to face thrilling events, meet fascinating characters, and even encounter wild animals. Every decision you make will shape your journey. Will you thrive as a brave adventurer or succumb to the dangers of the unknown? Let's find out!\n")

    health = 100
    inventory = []
    gold = 0
    explore_count = 0

    while health > 0:
        print("Your current stats:")
        print(f"Health: {health}")
        print(f"Inventory: {inventory}")
        print(f"Gold: {gold}\n")

        print("Choose an action:")
        print("1. Explore the area")
        print("2. Check your inventory")
        print("3. Rest (Regain some health)")
        print("4. Quit the game")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            explore_count += 1
            if explore_count % 3 == 0:
                damage = wild_animal_event()
                health -= damage
            else:
                event = random_event()
                print(f"\n{event}\n")
                if "treasure chest" in event:
                    gold_found = random.randint(10, 50)
                    print(f"You found {gold_found} gold!")
                    gold += gold_found
                elif "friendly traveler" in event:
                    item = random.choice(["Healing Potion", "Magic Scroll", "Sword"])
                    print(f"You received a {item}!")
                    inventory.append(item)
                elif "hidden trap" in event:
                    damage = random.randint(10, 20)
                    print(f"You lose {damage} health.")
                    health -= damage
                elif "magical fountain" in event:
                    heal = random.randint(15, 30)
                    print(f"You regain {heal} health.")
                    health = min(100, health + heal)
                elif "storm" in event:
                    print("You lose some time, but no health is lost.")
                elif "mysterious map" in event:
                    print("The map is added to your inventory.")
                    inventory.append("Mysterious Map")

        elif choice == "2":
            print("\nYour inventory contains:")
            if inventory:
                for item in inventory:
                    print(f"- {item}")
            else:
                print("Nothing yet. Keep exploring!")
            print()

        elif choice == "3":
            heal = random.randint(5, 15)
            print(f"You rest and regain {heal} health.\n")
            health = min(100, health + heal)

        elif choice == "4":
            print("\nThanks for playing the Random Adventure Game! Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.\n")

    if health <= 0:
        print("\nYou have perished on your adventure. Better luck next time!")

if __name__ == "__main__":
    main()

