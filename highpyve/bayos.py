from faker import Faker
from faker_animals import AnimalsProvider

fake = Faker()
fake.add_provider(AnimalsProvider)

def create_fake_animal_profile():
    print("\nAnimal Profile")
    print("Common Name: ", fake.animal_name())
    print("Scientific Name: ", fake.animal_name_scientific())
    animal = fake.animal()
    print("Class: ", animal['class'])