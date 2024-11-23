def caracter_infiltrado(cadena1, cadena2):

    if len(cadena1) != len(cadena2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    
    infiltrado = [] 
    
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            infiltrado.append(cadena2[i])
    
    return infiltrado


cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

try:
    resultado = caracter_infiltrado(cadena1, cadena2)
    print(f"Caracter infiltrado: {resultado}")
except ValueError as e:
    print(f"Error: {e}")
