import math

def degree_to_radian(D):
    R = (D * math.pi) / 180
    return R

D = float(input("Input Degree: "))
print("Output radian:", degree_to_radian(D))