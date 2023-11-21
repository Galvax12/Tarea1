valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))
suma = valor1 + valor2 + valor3

if suma % 7 == 0:
    print("La suma", suma,"de los valores es múltiplo de 7.")
else:
    print("La suma ",suma,"de los valores no es múltiplo de 7.")