#functions with outputs

def format_name(first_name, last_name):

  first_name = first_name[0].upper() + first_name[1:].lower()

  last_name = last_name[0].upper() + last_name[1:].lower()

  full_name = first_name + " " + last_name

  return full_name

print(format_name('suNdeeP','ARANdara'))

def format_name2(first_name, last_name):

  full_name = (first_name + " " + last_name).title()

  return full_name

print(format_name2('suNdeeP','ARANdara'))