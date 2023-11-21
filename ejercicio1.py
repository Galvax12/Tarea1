valor1 = float(input("Ingresa el primer valor: "))
valor2 = float(input("Ingresa el segundo valor: "))

# Comparar los valores
if valor1 > valor2:
    print("El primer valor es mayor que el segundo.")
    print("El segundo valor es menor que el primero.")
elif valor1 < valor2:
    print("El primer valor es menor que el segundo.")
    print("El segundo valor es mayor que el primero.")
else:
    print("Ambos valores son iguales.")
