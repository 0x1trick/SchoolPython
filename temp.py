import math
import numpy as np
"""
a=5

while a < 20:
    a+=5
    print(a)

"""
"""
a = 2
b = 3

c = a
a = b
b = c
print(a,b)
"""
"""
v_0 = 5 
a = 9.81
t = 4

s=v_0*t+1/2*a**2
print(s)
"""
"""
a=2
b=3

c=a/b

print(f"svaret {a} delt pa {b} blir {c:.2f}")
"""
"""
r = float(input("Oppgi radius: "))

A=3.14*r**2
print(f"{A:.3}")
"""
"""
a == b | likt
a !=   | ikke likt
a < b  | a mindre enn b
a >  b | a bigger than b
a <= b | a mindre enn eller like b

NOT every thing must be false to be true, and every thing must be true, or

INT = hel tall
FLOAT = ikke hel tall

% resten
// round til den beste tall
"""

# Oppg 15
"""
tall1 = float(input("Write your first nummber: "))
tall2 = float(input("Write ypur second nummber: "))

if tall1 == tall2:
    print("Both of theme are the same.")
else:
    print("They arent the same nummbers.")
"""
# Oppg 16
"""
User_input = int(input("La oss se om tallet er helltall eller partall: "))

if User_input % 2 == 0:
    print(f"{User_input} et helltall.")
else:
    User_input % 2 == 1
    print(f"{User_input} er et partall.")
"""
# Oppg 17
"""
tall1 = float(input("Skriv 1 tallet dit: "))
tall2 = float(input("Skriv 2 tallet dit: "))

if tall1 >= 0 and tall2 >= 0:
    print("Begge har like fortegn")
else:
    print("De har ikke like fortegn.")
"""


# random oppg
"""
Height = float(input("hva er din height(m): "))
Weight = float(input("hva er din weight(kg): "))

BMI = round(Weight / (Height * Height), 2)

if BMI <= 18.5:
    print("Du er undervektig")
elif BMI < 25:
    print("Du er Normalvektig")
else:
    BMI >= 25
    print("Du er Overvektig")

print(f"Din BMI er {BMI}")
"""


"""
En fnksjon gjør noe med det vi putter inn i funksjonen.

"""
"""
def area(r):
    print(3.14*r**2)
area(2)
"""
"""
def area(r):
    return 3.14*r**2
"""


"""
def trekant(g,h):
    return (g*h/2)\

svar = float(input("skriv grunnlingen: "))
svar2 = float(input("skriv høyden: "))

print(trekant(svar, svar2))
"""
"""
l = [2, 4, 6, 8, 10]
m = [1 , 3, 5, 9]
print(l * 2)
"""
"""
L = []
L.append(5)
L.append(2)
L.append(3)
L.append(6)
print(L[-1])
"""

"""
operasjoner i lister
l[i]
l[1:3]
len(l)
l.sort()
l.sort(reverse = true)
"""
"""
def f(x):
    return 2*x-2
def g(x):
    return x+3

x =-2

while f(x) != f(g):
    x=x+1

print(x)
"""
"""
svar1 = int(input("velg tall: "))

x = svar1
def f(x):
    return(2*x-2)

def g(x):
    return(x+2) 

while f(x) != g(x):
    x=x+1

print(x)
"""
"""
def gange(x, n):
    return(x*n)

c=float(input("skriv et tall: "))
d=float(input("skriv en annen tall: "))

print(gange(c,d))
"""
"""
def f(x):
    return(3*x**2+3)

c = float(input("Hva er dit x verdi?: "))

# MINDRE DESIMALER.
print(f"{f(c):.2f}")
"""
#26
"""
def f(x):
    return("HEllO " * x)
print(f(3))
"""
"""
def f(x,y):
    return(x+y)

a=3
b=4
print(f"{a}+{b}={f(a,b)}")
"""
"""
Liste = [0,1,2,3,4,5,6,7,8,9]

print(Liste)
"""
"""
#Append!
Liste = []

Liste.append('h1')
print(Liste)
"""
"""
Liste = []
Liste.append(1)
Liste.append(2)
Liste.append(333)
print(len(Liste))
"""
"""
L = [1,2,3,4,5,6,7,8,9,10]

a = L[2]
b = L[3]
c = L[4]

print(a,b,c)
"""
"""
L = []
L.append(5)
L.append(2)
L.append(3)
L.append(6)
print(L[2])
"""
"""
def radiussirkel(areal):
    return(math.sqrt(areal/math.pi))

print(f"{radiussirkel(100):.3f}")
"""
"""
Numpy har en datatype som kalles array. Det likner p[ et liste, men vi kan regne med verdiene i en arry, 
det vi ikke med verdiene i en liste. En liste er elemente adskilt med komma, det er ikke de i en array.
"""
"""
Liste1 =[3,1,2,3.5,6]
Liste =[1,0,10,44,56,0.3]

l1=np.arange(3,3.5,0.1)
print(l1)
l2=np.arange(0,1,0.2)
print(l2)

#print(Liste1+Liste)
print(l1+l2)
print(3*l2)
"""
"""
l3=np.linspace(3.0,3.5,12)

print(l3)
"""
"""
print(math.pi)
print(math.sqrt(15))
"""
import random
"""

print(random.random())
"""
'''
from math import sqrt

a= float(input("A NUM: "))
b= float(input("B NUM: "))
c= float(input("C NUM: "))

d=b**2-4*a*c  # angir formel for diskriminanten.

if d<0:
    print("likningen har ingen l;sning")

elif d==0:
    x=(-b)/(2*a)
    print("linking har bare 1 l;sning x=",x)

else:
    x1 = ((-b)+sqrt(d))/(2*a)
    x2 = ((-b)-sqrt(d))/(2*a)
    print("likningen har to l;sninger, x1=",x1,"og x2=",x2)
'''

import numpy
import matplotlib.pyplot as plt
'''
import math

r = float(input('skriv a: '))
silinder = float(input('hoyden: '))
Vol = (4*math.pi*r**3)/3

print(f'areal av sirkel {Vol:.3f}')
'''
'''
import numpy as np 
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y1 = [5,3,4,6,5,1]
y2 = [1,4,5,3,4,3]

plt.plot(x,y1, label="A-klassen")
plt.plot(x,y2, label="B-kalaseen")
plt.title("karakterer for to kalsser")
plt.xlabel("Karakterer")
plt.ylabel("Antall")
plt.grid()
plt.legend()
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return(2*x**2-8*x-4)

def g(x):
    return(-2*x+5)

#definerer x-verdierne, dvs. angir definisgonsmengde.

x = np.linspace(-1,5,6,)

plt.plot(x,f(x), label="f(x)")
plt.plot(x,g(x), label="g(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()
'''
'''
import numpy 
import matplotlib.pyplot as plt

x = [0,5,10,15]
y = [30,43,55,60]

plt.plot(x,y,"o")

plt.grid()
plt.show()
'''
'''
def f(x):
    return(x**2+3*x-4)

x = np.linspace(-5,5)

plt.plot(x,f(x), label="f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()
'''

#numerisk løsning av likninger, alle løsninger kan ses på som å finne nullpunktene til en funksjon.
#halveringsmetode for å finne nullpunkt
#forensetning: grafen er sammenhengen de i et intevall [a,b] og det er vare ett nullpunkt i intevallet.
'''
def f(x):
    return(x**2-3)

x = np.linspace(-4,6,1000)

plt.plot(x,f(x), label="f(x)")
plt.grid()
plt.axhline(y=0,color="k")
plt.axvline(x=0,color="k")




a=-2 #definerer nedre grense for intervallet
b=1 #definerer ovre grense for intervallet

noyaktighet = 0.001

m=(a+b)/2 #definerer midtpunkte

while b-a>noyaktighet:
    if f(a)*f(m)<0: #dersom det liger ett nullpunkt
        b=m 
    else:
        a=m
    m=(a+b)/2
print(f"løsningen av likninger er x={m:.3f}")

plt.show()
'''
'''
def  f(x):
    return(x**2-x-6)

x=np.linspace(-4,6,1000)

plt.plot(x,f(x))
plt.grid()

plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")

a=2
b=4

noyaktighet = 0.001
m=(a+b)/2

while b-a>noyaktighet:
    if f(m)==0:
        break
    if f(a)*f(m)<0: #dersom det liger ett nullpunkt
        b=m
    else:
        a=m
    m=(a+b)/2
print(f"losningn er x {m:.3f}")


plt.show()
'''

#4.33
'''
def f(x):
    return(x**2-2)

x = np.linspace(-4,6,1000)
plt.plot(x,f(x), label="f(x)")

plt.plot(x,f(x), label="f(x)")
plt.grid()
plt.axhline(y=0,color="k")
plt.axvline(x=0,color="k")
a = 0
b = 3

noyaktighet = 0.001
m=(a+b)/2
while b-a>noyaktighet:
    if f(m)==0:
        break
    if f(a)*f(m)<0: #dersom det liger ett nullpunkt
        b=m
    else:
        a=m
    m=(a+b)/2
print(f"losningn er x {m:.3f}")
plt.show()
'''
'''
# 4.34
def f(x):
    return(x**2-2*x-4)

x = np.linspace(-4,6,1000)
plt.plot(x,f(x), label="f(x)")

plt.plot(x,f(x), label="f(x)")
plt.grid()
plt.axhline(y=0,color="k")
plt.axvline(x=0,color="k")
a = -10
b = 0

noyaktighet = 0.001
m=(a+b)/2
while b-a>noyaktighet:
    if f(a)*f(m)<0: #dersom det liger ett nullpunkt
        b=m
    else:
        a=m
    m=(a+b)/2
print(f"losningn er x {m:.3f}")
plt.show()
'''
#4.35
'''
def f(x):
    return(x**2-3*x+1)

x = np.linspace(-4,6,1000)
plt.plot(x,f(x), label="f(x)")

plt.plot(x,f(x), label="f(x)")
plt.grid()
plt.axhline(y=0,color="k")
plt.axvline(x=0,color="k")
a = 0
b = 2
count = 0

noyaktighet = 0.001
m=(a+b)/2
while b-a>noyaktighet:
    if f(m)==0:
        count +=1
        break
    if f(a)*f(m)<0: #dersom det liger ett nullpunkt
        b=m
        count +=1
    else:
        a=m
        count +=1
    m=(a+b)/2

print(f"losningn er x {m:.3f}")
print(count)
plt.show()
'''
'''
#numerisk devirasjon
def f(x):
    return(x**2+3*x+6)

delta_x = float(input('Hvor stor er delta x? '))
a = float(input('Hvilken x-verdi vil du finne den deriverte til? '))

def df(a):
    return (f(a+delta_x)-f(a))/delta_x

print(f'Den deriverte er: {df(a):.3f}')

x= np.linspace(-5,3,1000)
y= f(x)
dy= df(x)

plt.plot(x,y,label="f(x)")
plt.plot(x,dy,label="f'(x)") # deriverte linje.
plt.grid()
plt.axhline(color="k")
plt.axvline(color="k")
plt.legend()
plt.title('Grafen og den deriverte')

plt.show()
'''
'''
5.27
def f(x):
    return(3*x**3-3*x**2+1)

delta_x = float(input('Hvor stor er delta x? '))
a = float(input('Hvilken x-verdi vil du finne den deriverte til? '))

def df(a):
    return (f(a+delta_x)-f(a))/delta_x

print(f'Den deriverte er: {df(a):.3f}')

x= np.linspace(-5,3,1000)
y= f(x)
dy= df(x)

plt.plot(x,y,label="f(x)")
plt.plot(x,dy,label="f'(x)") # deriverte linje.
plt.grid()
plt.axhline(color="k")
plt.axvline(color="k")
plt.legend()
plt.title('Grafen og den deriverte')

plt.show()
'''
'''
5.28
def f(x):
    return(-(1/2)*x**2+3*x-5)

delta_x = float(input('Hvor stor er delta x? '))
a = float(input('Hvilken x-verdi vil du finne den deriverte til? '))

def df(a):
    return (f(a+delta_x)-f(a))/delta_x

print(f'Den deriverte er: {df(a):.3f}')

x= np.linspace(-5,3,1000)
y= f(x)
dy= df(x)

plt.plot(x,y,label="f(x)")
plt.plot(x,dy,label="f'(x)") # deriverte linje.
plt.grid()
plt.axhline(color="k")
plt.axvline(color="k")
plt.legend()
plt.title('Grafen og den deriverte')

plt.show()
'''

'''
def f(x):
    return(2*x**2-4*x+1)

delta_x = float(input('Hvor stor er delta x? '))
a = -10
b = 0


def df(a):
    return (f(a+delta_x)-f(a))/delta_x

print(f'Den deriverte er: {df(a):.3f}')

x= np.linspace(-5,3,1000)
y= f(x)
dy= df(x)

plt.plot(x,y,label="f(x)")
plt.plot(x,dy,label="f'(x)") # deriverte linje.
plt.grid()
plt.axhline(color="k")
plt.axvline(color="k")
plt.legend()
plt.title('Grafen og den deriverte')

plt.show()
'''