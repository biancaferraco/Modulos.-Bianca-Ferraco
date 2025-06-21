import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculadora_indices as calc

#TMB_(actividad_fisica)
def actividad_fisica():
    print("Selecciona tu nivel de actividad física semanal:")
    print(" 1 Poco o ningún ejercicio. 1.2")
    print(" 2 Ejercicio ligero (1 a 3 días por semana). 1.375")
    print(" 3 Ejercicio moderado (3 a 5 días por semana). 1.55")
    print(" 4 Deportista (6 a 7 días por semana). 1.72")
    print(" 5 Atleta (entrenamientos mañana y tarde). 1.9")

    actividad = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.72,
        5: 1.9
    }

    while True:
        try:
            opcion = int(input("Ingrese un número del 1 al 5 según su nivel de actividad: "))
            if opcion in actividad:
                return actividad[opcion]
            else:
                print("Opción inválida. Por favor ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

print(f"\n Cálculo de Tasa metabólica basal según actividad física")  
try: 
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en cm: "))
    edad = int(input("Ingrese su edad: "))
    valor_genero = int(input("Ingrese 5 si es HOMBRE o -161 si es MUJER: "))
    valor_actividad = actividad_fisica()
    tmb_actividad_fisica = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"\nSu gasto  estimado segun su actividad física es de: {tmb_actividad_fisica:.2f} calorías/día")
except ValueError as e:
    print(f"No ingresaste los valores correctos {e}")
finally:
    print("\nCálculo de Tasa metabólica basal según actividad física finalizado.")