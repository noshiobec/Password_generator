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
pas_wd=""
for i in range(1,nr_letters +1):
  rnd_chr=random.choice(letters)
  pas_wd+=rnd_chr

for j in range(1,nr_numbers +1):
  rnd_nm=random.choice(numbers)
  pas_wd +=rnd_nm

for k in range(1,nr_symbols +1):
  rnd_sym=random.choice(symbols)
  pas_wd +=rnd_sym

print(f"Your password should be  {pas_wd}")

#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#This gives a better password Generator
pas_wd=[]
for i in range(1,nr_letters +1):
  rnd_chr=random.choice(letters)
  pas_wd.append(rnd_chr)

for j in range(1,nr_numbers +1):
  pas_wd.append(random.choice(numbers))

for k in range(1,nr_symbols +1):
  pas_wd.append(random.choice(symbols))
 
print(pas_wd)
random.shuffle(pas_wd)
print(pas_wd)

password=''
for char in pas_wd:
  password+=char
print(f"Your password is {password}.")



