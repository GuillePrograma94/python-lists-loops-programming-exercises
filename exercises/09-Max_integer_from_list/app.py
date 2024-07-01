my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(lista):
    valor_a_comparar = lista[0]
    for i in range(len(lista)):
        if valor_a_comparar < lista[i]:
            valor_a_comparar = lista[i]
           
    return valor_a_comparar

print(max_integer(my_list))
