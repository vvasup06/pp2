
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

def trapeziol(func,upper,lower,n):
    d = (upper-lower)/n
    result = (func(lower) + func(upper))
    for i in range (1,n):
        result += 2 * func(lower + (i*d))
    return result


func_str = input("Write a function 'for example lambda x: x**2' : ")
function_definition = func_str.split(':', 1)[1].strip()
function = sympify(function_definition)



func = eval(func_str)
upper = int(input("Upper bound :"))
lower = int(input("Lower bound :"))
n = int(input("Numbers of subintervals :"))
T = trapeziol(func,upper,lower,n)
dx=(upper-lower)/n
print ("T:",T*(dx)/2)
trap = T*(dx)/2

x = symbols('x')
M = diff(diff(function_definition,x)) 
print("Second derivative is:", M)
Etm = 0
if M == 0:
    Etm = 0
elif M != 0:
    Etm = (M*((upper - lower)**3))/(12*(n**2))
print("|E| = ",Etm)   
x = symbols('x')
integral = integrate(function_definition, (x,lower,upper))
print("Integral =", integral)
Et = trap - integral
print("Et = ", Et)
percenterror = (Et/integral)*100
print("percent:", percenterror)

valx = np.linspace(lower, upper, 100)
numeric_func = lambdify(x, function, modules=['numpy'])
valy = np.array([numeric_func(i) for i in valx], dtype=float)

plt.plot(valx, valy, label=func_str)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the Function')
plt.legend()
plt.grid(True)
plt.show()