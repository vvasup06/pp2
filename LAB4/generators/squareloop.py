a = float(input("Write a: "))
b = float(input("Write b: "))
i = a
for i in range(int(a), int(b)):
    print(i * i, end=", ")
    i += 1