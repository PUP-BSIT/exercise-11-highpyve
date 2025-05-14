from faker import Faker

fake = Faker()

def create_fake_profile():
    print("\nName: ", fake.name())
    print("Email: ", fake.email())
    print("Address: ", fake.address())
    print("Phone Number: ", fake.phone_number())
    print("Job: ", fake.job())
    print("Date of Birth: ", fake.date_of_birth(minimum_age=18, 
                                                maximum_age=50))
    

