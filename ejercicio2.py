valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))

if valor1 > valor2 and valor1 > valor3:
    print("El mayor valor es:", valor1)
elif valor2 > valor1 and valor2 > valor3:
    print("El mayor valor es:", valor2)
if valor3 > valor1 and valor3 > valor2:
    print("El mayor valor es:", valor3)
else:
    print("los tre son iguales.")