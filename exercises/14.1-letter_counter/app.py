par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
#limpiamos la lista, quitando los espacios y dejándolo todo en minúsculas:
par_limpio = par.replace(" ","").lower()
for letter in par_limpio:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1
    
print(counts)
