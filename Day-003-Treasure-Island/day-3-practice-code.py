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