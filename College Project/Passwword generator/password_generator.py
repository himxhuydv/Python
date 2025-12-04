import string  
import random
print("Hello Sir,Welcome to Password Generator")
# Creating list 
letter =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeric =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_character =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

password=[]
Alphabet_input=int(input("Enter the number of alphabets required in the password a,b,c,d...z\n"))
Numeric_input=int(input("Enter the number of numeric values required in the password 1,2,3,4..9\n"))
Special_character_input=int(input("Enter the number of special characters required '!', ', '#', '$', '%' ..etc\n"))

# useing for loop  for acessing the value:
for i in range(Alphabet_input):
    password.append(random.choice(letter))
for i in range(Numeric_input):
    password.append(random.choice(numeric))
for i in range(Special_character_input):
    password.append(random.choice(special_character))

# Randomizing the password using shuffle:
random.shuffle(password)
final_password="".join(password)
print("Thank you For using Password Generator.Here is your generated Password\n",final_password)
