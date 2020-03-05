import math as mt
a=input("ingrese el valor de a: ")
a=float(a)
theta=input("ingrese el valor de theta: ")
theta=float(theta)
#theta=(theta*mt.pi)/180
x=a*(mt.cos(theta))
y=a*(mt.sin(theta))
print("x es: ",x)
print("y es: ",y)
