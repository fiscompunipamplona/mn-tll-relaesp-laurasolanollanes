import math as mt
c=3e8
ly=9.461e15
x=input("ingrese la distancia en años luz de un planeta al otro: ") #1ly=9.461e15m
x=float(x)
x=x*ly
v=input("ingrese la velocidad con la que se mueve la nave: ") #m/s como fraccion de c.
v=float(v)
#v=v*(c) #m/s
#gamma=(1/(mt.sqrt(1-(v**2))))
t1=x/(v*c)
t2=(t1-((v*x)/(c)))/mt.sqrt(1-(v**2))
print("desde la nave tarda en sgundos: ",t1)
print("desde la tierra tarda en segundos: ",t2)
