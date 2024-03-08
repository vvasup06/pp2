def tr_area(h, a, b):
    return (a + b) / 2 * h

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = tr_area(height, base1, base2)
print("Expected Output:", area)  
