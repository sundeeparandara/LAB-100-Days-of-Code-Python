from prettytable import PrettyTable

table = PrettyTable()

#print(table)
#print(type(table))

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"

print(table)