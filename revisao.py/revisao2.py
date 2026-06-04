frutas = ["Banana", "Maçã","Tomate", "Laranja", "Melancia"]
verduras = ["Alface","Repolho","Acelga"]
print("Bem Vindo ao montador de saladas!")
print("Aqui você poderá montar sua salada favorita!")
print()
print ("Primeiramente, você quer ver as frutas ou verduras?")
print("1 - Frutas   |    2 - Verduras")
opcao = input("Escolha dentre as opções (1 ou 2):")
match opcao:
    case "1":
        for index,fruta in enumerate(frutas):
            print(f"Fruta #{index+1}: {fruta}")
    case "2":
        for index,verdura in enumerate(verduras):
            print(f"Verdura #{index+1}: {verdura}")
print("Digite o número do ingrediente que você deseja!: ")
index_ingrediente = int(input("Número: "))-1
ingrediente = ""
if opcao == "1":
    ingrediente = frutas[index_ingrediente]
elif opcao == "2":
    ingrediente = verduras[index_ingrediente]
print(f"Você adicionou {ingrediente} à salada!")