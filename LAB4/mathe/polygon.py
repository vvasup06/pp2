import math

def area(number, length):
    return number * length ** 2 / (4 * math.tan(math.pi / number))

number = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

print("Area:", int(area(number, length)))