
def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?\n")

greet()

#############

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"Isn't the weather nice today...{name}?\n")

greet_with_name("Pikachu")

##############

#positional argument
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What's it like in {location}?\n")

greet_with("Pikachu","Pallet Town")

###############

#keyword argument
def greet_with_k(location="Pallet Town",name="Pikachu"):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What's it like in {location}?\n")

greet_with_k(location="Pewter City", name="Geodude")
greet_with_k(name="Geodude",location="Pewter City")
greet_with_k("Geodude","Pewter City")
greet_with_k()
