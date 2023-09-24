#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

new_password = []
# latters_list = random.randint(0,nr_letters)
# print(latters_list)
# for l in range(0,nr_letters):
#   new_letter= letters[l]
#   print(new_letter)

# random_Value = 0
# for r in range(0,nr_letters):
#   random_Value = random.randint(0,r)
#   # print(random_Value)
#   # print("")
#   new_letter = letters[random_Value]
#   print(new_letter)



for char in range(1,nr_letters+1):
  new_password.append(random.choice(letters))
for char in range(1,nr_symbols+1):
  new_password.append(random.choice(symbols))
for char in range(1,nr_numbers+1):
  new_password.append(random.choice(numbers))

# print(new_password)

random.shuffle(new_password)

# print(new_password)

password =""
for char in new_password:
  password += char

print(f"Your PassWord is: {password}")