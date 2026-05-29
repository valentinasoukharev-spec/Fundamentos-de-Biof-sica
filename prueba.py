
import Modulobiofisica as mb 
def fun1 (x):
    return x**2
x1 = 6
h= 0.1
print(mb.derivada_diferencia_centrada(fun1,x1, h))
print(mb.integral_simpson(fun1, 1,10, 6))