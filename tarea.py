import math

def calcular_hipotenusa(a, b):
    hipotenusa = math.sqrt(a^2 + b^2)
    return hipotenusa

a = float(input("Ingrese el primer cateto: "))
b = float(input("Ingrese el segundo cateto: "))

print(calcular_hipotenusa(a, b))