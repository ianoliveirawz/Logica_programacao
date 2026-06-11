import time
print("********** Média de notas **********")
print("************************************")
print("Aqui você poderá vizualizar sua média" \
" e saber em que situação se encontra:)")
time.sleep(3)
print("Primeiro coloque cinco notas abaixo.")
time.sleep(2)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))
media = ( nota1 + nota2 + nota3 + nota4 + nota5 )/ 2
time.sleep(3)
if media >= 7:
    situacao = "Aprovado, parábens"
elif media >= 5:
    situacao = "Recuperação, tome cuidado!!!"
else:
    situacao = "Reprovado, boa sorte na próxima"

print(f"Média: {media}")
print(f"Situação: {situacao}")