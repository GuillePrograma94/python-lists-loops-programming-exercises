# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below
def generate_random():
    for i in range(10):
        random_value = random.randint(1,1000)
        my_list.append(random_value)

    return my_list

generate_random()

print(my_list)