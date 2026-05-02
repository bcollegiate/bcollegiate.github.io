import os
import random
import string
def generate_random_string(length):
    """
    Generate a random string of fixed length.
    """
    # Define the possible characters
    characters = string.ascii_letters + string.digits
    # Generate the string using a list comprehension and join them
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
length = 10
my_string = generate_random_string(length)
os.system('git add .')
os.system(f'git commit -m "{my_string}"')
os.system('git push origin main')
