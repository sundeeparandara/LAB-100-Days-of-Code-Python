#1. Create a greeting for your program.
print('Welcome to Band Name Generator!!!')

#2. Ask the user for the city that they grew up in.
hometown = input('Where did you grow up?\n')

#3. Ask the user for the name of a pet.
petname = input("What is your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
bandname = hometown + " " + petname
print('Your Band Name is : {}'.format(bandname))
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/