number = float(input("Write a number: "))
i = 0
while i <= number:
    if i % 2 == 0:
        print(i, end=", ")
    i += 1