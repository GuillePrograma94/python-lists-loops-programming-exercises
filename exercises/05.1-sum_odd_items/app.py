my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    total = 0
    for i in range(len(list)):
        if (list[i] % 2) != 0:
            total = total + list[i]
    
    return total

print(sum_odds(my_list))