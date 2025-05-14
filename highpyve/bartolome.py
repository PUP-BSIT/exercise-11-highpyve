from pyjokes import get_joke

def get_jokes():
    user_input = input("Do you want to read a joke? (Y/N): ").strip().lower()
    if user_input == 'y':
        print(get_joke())
    elif user_input == 'n':
        print("Okay, thanks!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

get_jokes()
