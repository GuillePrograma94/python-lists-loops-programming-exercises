# Your code here
x = 20
while x != -1:
  if x % 5 == 0 and x != 0:
    print(str(x) + "!")
    x -= 1
  elif x >= 1:
    print(x)
    x -= 1
  else:
    print("LIFTOFF")
    break