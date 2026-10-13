# 5. Resolver ecuación ax + b = 0


a = float(input("Introduce el valor de 'a': "))
b = float(input("Introduce el valor de 'b': "))

if a != 0:
    x = -b / a
    print(f"La solución de la ecuación es: x = {x}")
else:
    print("Error: No se puede dividir por cero. 'a' no puede ser 0.")