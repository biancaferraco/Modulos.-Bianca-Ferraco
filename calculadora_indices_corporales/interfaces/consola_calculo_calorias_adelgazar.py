import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculadora_indices as calc

print("Calculo de calorías recomendadas para adelgazar")
print(f"\nPara adelgazar, se recomienda reducir el consumo diario entre un 15% y 20% de la Tasa Metabólica Basal (TMB).")

try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en cm: "))
    edad = int(input("Ingrese su edad: "))
    valor_genero = int(input("Ingrese 5 si es HOMBRE o -161 si es MUJER: "))
    
    mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(mensaje)

except ValueError as e:
    print(f"Error en la entrada de datos: {e}")
finally:
    print("\nCálculo de calorías recomendadas para adelgazar finalizado.")