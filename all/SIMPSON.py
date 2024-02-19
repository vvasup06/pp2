from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

def trapeziol(func, upper, lower, n):
    d = (upper - lower) / n
    result = (func(lower) + func(upper))

    for i in range(1, n):
        if i % 2 == 0:  
            result += 2 * func(lower + (i * d))
        else:  
            result += 4 * func(lower + (i * d))
    
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
print ("T:",T*(dx)/3)
trap = T*(dx)/3

x = symbols('x')
M = diff(diff(diff(diff(function_definition, x), x), x), x)
print("Fourth derivative is: ", M)
Esm = 0
if M == 0:
    Esm = 0
elif M != 0:
    Esm = (M*((upper - lower)**5))/(180*(n**4))
print("|E| = ",Esm)   
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



