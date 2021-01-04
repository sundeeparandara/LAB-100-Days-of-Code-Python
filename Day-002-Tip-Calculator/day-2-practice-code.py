# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0])+int(two_digit_number[1]))


####################################################


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(float(weight) / float(height)**2)
print(bmi)

###########################################################

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

yr = 90 - age

dr = yr * 365
wr = yr * 52
mr = yr * 12

print(f"You have {dr} days, {wr} weeks and {mr} months left.")