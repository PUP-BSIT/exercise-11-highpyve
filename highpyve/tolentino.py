import getname

def get_cat_name(owner_name):
    """Generates a random cat name and prints it with the owner's name."""
    cat_name = getname.random_name('cat')
    print(f"{owner_name}, your cat's name is {cat_name}.")
    
    return cat_name