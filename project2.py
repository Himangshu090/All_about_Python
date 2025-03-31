#Random Password Generator
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ""
pass_length = int(input("Enter a length of password you want: "))

#Using for loop
"""for i in range(pass_length):
    password+=random.choice(characters)"""

#Using list comprehension
password = "".join([random.choice(characters) for i in range(pass_length)])

print("Your new random password is", password)


