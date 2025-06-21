import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculadora_indices as calc

print(f"\n Cálculo de calorías en reposo (TMB)")  

try:  
    peso = float(input("Ingrese su peso en kg: "))  
    altura = float(input("Ingrese su altura en centimetros: "))  
    edad = int(input("Ingrese su edad: "))  
    valor_genero = int(input("Ingrese 5 si es HOMBRE o -161 si es MUJER: "))  
    tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print(f"\nSu TMB (calorías en reposo) es: {tmb:.2f} calorías/día")
except ValueError as e:
    print(f"No ingresaste los valores correctos {e}.")
finally:
    print("\nCálculo de calorías en reposo finalizado.")