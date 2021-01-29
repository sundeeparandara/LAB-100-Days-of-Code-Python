from replit import clear
from art import logo

print(logo)
a = float(input("What's the first number?: "))
print("+\n-\n*\n/")
ops = input("Pick an operation: ")
b = float(input("What's the next number?: "))

def add(a,b):
  return a+b

def substract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

def call_calc(a,b,ops):
  output = 0
  if ops == "+":
    output = add(a,b)
    print(f"{a} {ops} {b} = {output}")
  elif ops == "-":
    output = substract(a,b)
    print(f"{a} {ops} {b} = {output}")
  elif ops == "*":
    output = multiply(a,b)
    print(f"{a} {ops} {b} = {output}")
  elif ops == "/":
    output = divide(a,b)
    print(f"{a} {ops} {b} = {output}")
  else:
    print("invalid operation")
  return output



while True:
  output = call_calc(a,b,ops)
  continue_calc = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
  if continue_calc == 'y':
    a = output
    ops = input("Pick an operation: ")
    b = float(input("What's the next number?: "))
  else:
    clear()
    print(logo)
    a = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    ops = input("Pick an operation: ")
    b = float(input("What's the next number?: "))   

