import math

def calcular_hipotenusa():
    a = float(input("Ingrese el primer ctaeto: "))
    b = float(input("Ingrese el segundo cateto: "))
    hipotenusa = math.sqrt(a^2 + b^2)
    print(f"La hipotenusa es: {hipotenusa}")


calcular_hipotenusa()