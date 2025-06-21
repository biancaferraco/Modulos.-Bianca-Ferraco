def calcular_IMC (peso: float, altura: float) -> float:
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso y altura deben ser mayores a cero.")
    imc = peso / (altura ** 2)
    return imc

def calcular_porcentaje_grasa (peso: float, altura: float, edad: int, valor_genero: float) -> float:
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    else:
        imc = calcular_IMC(peso, altura)  
        porcentaje_grasa = (1.2 * imc) + (0.23 * edad) - 5.4 - valor_genero
        return porcentaje_grasa

def calcular_calorias_en_reposo (peso: float, altura: float, edad: int, valor_genero: int) -> float:
    if peso <= 0:
        raise ValueError("El peso debe ser mayor a cero.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor a cero.")
    if edad <= 0:
        raise ValueError("La edad debe ser mayor a cero.")
    if valor_genero not in [5, -161]:
        raise ValueError("El valor de género debe ser 5 (hombre) o -161 (mujer).")
 
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb

def calcular_calorias_en_actividad(
    peso:float, altura:float, edad:int, valor_genero:int,
    valor_actividad:float
    )-> float:
    if not (1.2 <= valor_actividad <= 1.9):
        raise ValueError("El valor de actividad física debe estar entre 1.2 y 1.9.")
    tmb= calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_actividadfisica= tmb * valor_actividad
    return tmb_actividadfisica

def consumo_calorias_recomendado_para_adelgazar(
    peso: float,
    altura: float,
    edad: int,
    valor_genero: int
) -> str:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.80
    rango_superior = tmb * 0.85
    mensaje = (
        f"Para adelgazar es recomendado que consumas entre: "
        f"{int(rango_inferior)} y {int(rango_superior)} calorías al día."
    )
    return mensaje


   