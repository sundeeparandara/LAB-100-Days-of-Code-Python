programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)
print("\n")

#fetch
print(programming_dictionary["Bug"])
print("\n")

#add
programming_dictionary["Loop"] = "The action doing something over and over again."

print(programming_dictionary)
print("\n")

#create empty dict.
empty_dict = {}
print(empty_dict)
print("\n")

#wipe dict.
programming_dictionary2 = programming_dictionary
programming_dictionary2 = {}

print(programming_dictionary)
print("\n")
print(programming_dictionary2)
print("\n")

#edit dict.
programming_dictionary["Bug"] = "Butterfree"
print(programming_dictionary)
print("\n")

#loop through dict. - method 1
for key in programming_dictionary:
  val = programming_dictionary[key]
  print(f"{key} --> {val}")

print("\n")

#loop through dict. - method 2
print(programming_dictionary.items())
#print("\n")
print(type(programming_dictionary.items()))
#print("\n")
for key, val in programming_dictionary.items():
  print(f"{key} --> {val}")


