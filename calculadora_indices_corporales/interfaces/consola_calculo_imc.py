import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculadora_indices as calc

def clasificar_imc(imc):
    if imc < 16:
        return "Delgadez severa"
    elif imc < 17:
        return "Delgadez moderada"
    elif imc < 18.5:
        return "Delgadez aceptable"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    elif imc < 50:
        return "Obesidad tipo III o mórbida"
    else:
        return "Obesidad tipo IV o extrema"

print(f"\n Calculo del IMC")
try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calc.calcular_IMC(peso, altura)
    categoria = clasificar_imc(imc)

    print(f"\nSu IMC es: {imc:.2f}")
    print(f"Categoría: {categoria}")
    
except ValueError:
        print(f"\n Ingrese valores numéricos válidos para peso y altura.")
    
finally:
        print("\nProceso de cálculo de IMC finalizado.")
