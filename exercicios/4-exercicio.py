letras = []
consoantes = []

for i in range(0,10):
    letra = input("Digite uma letra: ")
    letra = letra.lower()
    letras.append(letra)
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        consoantes.append(letra)

print(f"Foram digitadas {len(consoantes)} consoantes")
print(f"As consoantes digitadas foram {consoantes}")