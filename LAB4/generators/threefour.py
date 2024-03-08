number = float(input("Wirte a number: "))
i = 0
while i <= number:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=",")
    i+=1 