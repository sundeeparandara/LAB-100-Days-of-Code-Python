#Write your code below this row 👇

for val in range (1,101):
  if ((val % 3 == 0) & (val % 5 == 0)):
    print("FizzBuzz")
  elif (val % 3 == 0):
    print("Fizz")
  elif (val % 5 == 0):
    print("Buzz")
  else:
    print(val)
