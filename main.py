from highpyve import tolentino, ocariza, anipan, bayos, bartolome

def pause():
    input("Press Enter to continue...")

print("Prints a personalized cat name based on the user's name")
print("=" * 50)
user_name = input("Enter your name to generate your cat's name: ")
capitalized_username = user_name.title()
tolentino.get_cat_name(capitalized_username)
print("=" * 50 + "\n")
pause()

print("\nGenerates a birthday summary showing how old the user is")
print(ocariza.birthday_summary())
print("=" * 50 + "\n")
pause()

print("\nCreates a randomly generated fake person profile")
print("=" * 50)
anipan.create_fake_profile()
print("=" * 50 + "\n")
pause()

print("\nCreates a fake animal profile")
print("=" * 50)
bayos.create_fake_animal_profile()
print("=" * 50 + "\n")
pause()

print("\nPrints random jokes for fun and laughter")
print("=" * 50)
bartolome.get_jokes()
print("=" * 50 + "\n")