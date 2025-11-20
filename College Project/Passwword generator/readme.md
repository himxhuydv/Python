# Password Generator – Python Project  
Wait.. wait ..   
As we jump to the technicality let's know the basics.
### What is Password?   
A password is a secret string of characters (which can include letters, numbers, and symbols).
### why do we need that.  
To verify A user's identity and grant them access to a secured resource, such as a computer system, website, device, or protected data.
## Password Generator   
This project is a random password generator written in Python.
It allows the user to choose how many alphabets, numbers, and special characters they want in the password, and then generates a fully randomized, secure password.

### Features  

Choose number of alphabets (a–z, A–Z)
Choose number of numeric digits (0–9)
Choose number of special characters (!, @, %, #, etc.)
Uses Python's random module for randomness
Final password is shuffled and printed as a single string
Clean and simple logic — easy for beginners to understand

### Project Structure

password_generator.py → Main program
readme.md → Documentation file

#### How the Code Works
1. Import Modules

import string
import random

string provides alphabets and digits (not used directly in your code but imported).
random is used to randomly pick characters.

2. Create Character Lists

letter = ['a', 'b', ... 'Z']
numeric = ['0', '1', ... '9']
special_character = ['!', '"', '#', ... '~']

These lists store:
Lowercase + uppercase letters
Numbers
Special characters
You pick from these lists randomly later.

3. Take Input From User

Alphabet_input = int(input(...))
Numeric_input = int(input(...))
Special_character_input = int(input(...))

The user decides how many:
Letters
Numbers
Special characters
they want in their password.

4. Generate Password

You add random characters from each list:

for i in range(Alphabet_input):
  password.append(random.choice(letter))

Same for numbers and special characters.

5. Shuffle the Password

random.shuffle(password)

This mixes letters, numbers, and symbols randomly.

6. Convert List → String

final_password = "".join(password)

Now the password looks like:
fG4$w7&Q

—not like a Python list.

7. Print Final Password

print("Here it's Your New Generated Password\n", final_password)

#### Sample Output

Hello Sir, Welcome to Password Generator
Enter the number of alphabet you want in the password:
5
Enter the number of numeric values you want:
3
Enter the number of special characters:
2

Thank you for using Password Generator.
Here it's Your New Generated Password:
gP4@Zq!7

