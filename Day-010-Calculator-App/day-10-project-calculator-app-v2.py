from art import logo

def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2
  
def multiply(n1,n2):
  return n1*n2
  
def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))

  for symbol in operations:
    print(symbol)

  should_continue = True #flag

  while should_continue:

    operations_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operations_symbol] #loading a function that is in the dictonary mag
    answer = calculation_function(num1, num2)

    print(f"{num1} {operations_symbol} {num2} = {answer}")

    if input(f"Type 'y' continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator() #recurssion

calculator()