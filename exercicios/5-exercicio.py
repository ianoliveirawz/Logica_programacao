numeros = []
pares = []
impares = []

for i in range(0,20):
    numero = int(input("Digite um numero inteiro:"))
    print()
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"O vetor inteiro é {numeros}")
print(f"Os valores par são {pares}")
print(f"Os valores ímpares são {impares}")