print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos una función para solicitar números de la lotería y mostrarlos ordenados
def obtener_numeros_triunfadores():
    # Inicializamos una lista vacía para almacenar los números
    numeros = []

    # Preguntamos cuántos números va a ingresar el usuario
    cantidad = int(input("¿Cuántos números triunfadores de la lotería desea ingresar? "))

    # Recolectamos los números ingresados por el usuario
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número triunfador {i + 1}: "))
        numeros.append(numero)

    # Ordenamos la lista de números de menor a mayor
    numeros.sort()

    # Mostramos la lista de números ordenada
    print("Números triunfadores de la lotería (de menor a mayor):")
    print(numeros)

# Llamamos a la función para ejecutar el programa
obtener_numeros_triunfadores()
