def validar_entrada(valor):
  try:
    numero = int(valor)
    if numero >= 1 and numero <= 10:
      return print("El valor introducido es válido.")
    else:
      return print("El valor introducido no es válido.")
  except ValueError:
    return print("El valor introducido no es válido.")

def calcular_promedio(numeros):
  if len(numeros) == 0:
    return None
  else:
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return print("El promedio de la lista es:", promedio)