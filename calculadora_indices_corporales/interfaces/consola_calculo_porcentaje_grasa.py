import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculadora_indices as calc
  
RANGOS_GRASA_RECOMENDADOS = {  
    "20-29": {10.8: "11% - 20%", 0: "16% - 28%"},  
    "30-39": {10.8: "12% - 21%", 0: "17% - 29%"},  
    "40-49": {10.8: "14% - 23%", 0: "18% - 30%"},  
    "50-59": {10.8: "15% - 24%", 0: "19% - 31%"}  
}  
  
def rango_recomendado_grasa(edad: int, valor_genero: float):  
    if valor_genero not in [10.8, 0]:  
        raise ValueError("Género debe ser 10.8 para hombre o 0 para mujer.")  
  
    if 20 <= edad <= 29:  
        rango_edad = "20-29"  
    elif 30 <= edad <= 39:  
        rango_edad = "30-39"  
    elif 40 <= edad <= 49:  
        rango_edad = "40-49"  
    elif 50 <= edad <= 59:  
        rango_edad = "50-59"  
    else:  
        return "Edad fuera de rango."  
  
    rango = RANGOS_GRASA_RECOMENDADOS[rango_edad][valor_genero]  
    genero= "masculino" if valor_genero == 10.8 else "femenino"
    return f"Para género {genero} y edad {rango_edad}, el porcentaje de grasa corporal recomendado es: {rango}"  
  
print(f"\n Cálculo de porcentaje de grasa corporal")  
  
try:  
    peso = float(input("Ingrese su peso en kg: "))  
    altura = float(input("Ingrese su altura en metros: "))  
    edad = int(input("Ingrese su edad: "))  
    valor_genero = float(input("Ingrese 10.8 si es HOMBRE o 0 si es MUJER: "))  
  
    porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)  
    rango_recomendado = rango_recomendado_grasa(edad, valor_genero)  
  
    print(f"\nSu porcentaje de grasa corporal es: {porcentaje_grasa:.2f}%")  
    print(rango_recomendado)  
  
except ValueError as e:  
    print(f"Error en la entrada de datos: {e}.")
finally:
    print("\nCalculo de porcentaje de grasa corporal finalizado.") 
