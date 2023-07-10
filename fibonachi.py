x = int(input(""))

first = 1
second = 1
while x > 2:
    sum = first + second
    first = second
    second = sum
    x = x - 1
print(second)
