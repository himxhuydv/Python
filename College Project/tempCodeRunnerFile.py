import string  # to use the string.ascii_lowercase we import string.
# import random # randome module for random password generation
# print("Hello Sir,Welcome to Password Generator")
# letter: why ascii_lowercase? For getting whole alphabet in a list.
letter =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(letter)  # use this for checking everything is working or not.

# If you want to know what ascii_lowercase is or how my code works, you can check the README:

#  Documentation: 
#Click here → [readme.md](./readme.md)

numeric =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_character = list(string.punctuation)
print(special_character)