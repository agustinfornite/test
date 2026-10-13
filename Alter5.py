#Introducir una letra, si es A visualizaremos el area de una circunferencia, si es L, visualizaremos la longitud de una circunferencia
import math
radio=float(input("dame un radio:"))
letra=input("dame una letra")

if letra=="a":
    a=math.pi*radio**2
    print(a)
elif letra=="l":
    l=2*math.pi*radio
    print(l)
else:
    print("error")
    
          
    
    
    