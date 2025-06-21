import math

def calcular_hipotenusa(a,b): 
    hipotenusa = math.sqrt(a**2 + b**2)
    print(f"La hipotenusa es: {hipotenusa}")

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

a = float(input("Ingrese el primer cateto: "))
b = float(input("Ingrese el segundo cateto: "))
calcular_hipotenusa(a,b)
calcular_area_triangulo(a, b)

