# # Standard Global & Local Scope

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(enemies)

# increase_enemies()
# print(enemies)

# # Modifying Global Scope <--- below doesn't work

# enemies = 1

# def increase_enemies():
#   enemies += 1
#   print(enemies)

# increase_enemies()
# print(enemies)

# Modifying Global Scope <--- below WORKS

enemies = 1

def increase_enemies():
  global enemies #<--- explicitly declares that there is a global variable called 'enemies' defined outside the perimeter of this function
  enemies += 1
  print(enemies)

increase_enemies()
print(enemies)