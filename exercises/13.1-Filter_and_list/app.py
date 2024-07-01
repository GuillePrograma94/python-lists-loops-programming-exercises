all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here

def my_function(names):
    return names[0] == 'r' or names[0] == 'R'

resulting_names = list(filter(my_function,all_names))

print(resulting_names)