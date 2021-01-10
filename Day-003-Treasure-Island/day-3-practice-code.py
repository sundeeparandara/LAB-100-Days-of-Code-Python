print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("Can ride")
else:
  print("Can't ride")


###############################################

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if ((number % 2) == 0):
  print("This is an even number.")
else:
  print("This is an odd number.")



############################

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


BMI = int(round(weight/height**2,0))

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")


############################################

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 != 0:
  print('Not a Leap Year.')
else:
  if year % 100 != 0:
    print('Leap Year.')
  else:
    if year % 400 == 0:
      print('Leap Year.')
    else:
      print('Not a Leap Year.')


###############################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

size = size.upper()
add_pepperoni = add_pepperoni.upper()

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
else:
  print("There is an error in your input")

extra_cheese = extra_cheese.upper()
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${int(bill)}.")

######################################################

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
name = name1+name2

count_name_true = 0
count_name_love = 0

for i in "true":
  freq = name.count(i)
  count_name_true += freq

for j in "love":
  freq = name.count(j)
  count_name_love += freq

score = int(str(count_name_true)+str(count_name_love))

if ((score < 10) | (score > 90)):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif ((score >= 40) & (score <= 50)):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")