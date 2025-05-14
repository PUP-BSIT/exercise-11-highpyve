from highpyve import tolentino, ocariza, anipan, bayos, bartolome

print("Rose Tolentino")
print("=" * 50)
user_name = input("Enter your name to generate your cat's name: ")
capitalize_username = user_name.title()
tolentino.get_cat_name(capitalize_username)
print("=" * 50 + "\n")

print("Jaira Ocariza")
print(ocariza.birthday_summary())
print("=" * 50 + "\n")

print("Kristoffer Anipan")
anipan.create_fake_profile()
print("=" * 50 + "\n")

print("Eurielle Bayos")
bayos.create_fake_animal_profile()
print("=" * 50 + "\n")

print("Bartolome's Jokes")
bartolome.get_jokes()
print("=" * 50 + "\n")