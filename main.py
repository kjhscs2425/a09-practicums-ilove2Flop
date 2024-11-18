def choose_practicum():
    practicums = ["Costumes", "Scenery", "Lighting", "Sound"]
    print("Available practicums: Costumes, Scenery, Lighting, Sound")
    choice = input("Please choose a practicum: ").capitalize()
    if choice in practicums:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return choose_practicum()

def signup_process():
    name = input("Enter your name: ").strip()
    practicum = choose_practicum()
    print(f"Congratulations, {name}, you are signed up for {practicum}!")

# Run the signup process
signup_process()
