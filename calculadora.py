print ("|-----------------------|")
print ("|       Cauculadora     |")
print ("|-----------------------|")
print ()
print ("Essa calculadora, faz todas as operações")
print ("A partir de dois números que você informar")
print ()

print ("Digite o valor correspondente ao cálculo")
print ("Que você quer fazer")
print()
print ("1 - As 4 operações")
print ("2 - Média de 3 valores")
print ("3 - Fórmula de Bháskara")
print()
opcao = int(input("Digite a opção: "))

match opcao :
    case 1:
        first_num = float(input("Digite o primeiro número:"))
        second_num = float(input("Digite o segundo número:"))
        print()


        adicao = first_num + second_num
        print ("A adição resulta em: ",adicao)
        print()

        subtracao = first_num - second_num
        print ("A subtração resulta em: ",subtracao)
        print()

        multi = first_num * second_num
        print (f"A multiplicação resulta em {multi} ")
        print()

        #Verificando se o segundo número é diferente de 0
        if second_num != 0:
            divisao = first_num / second_num
            print (f"A divisão resulta em {divisao}")
        else:
            print ("A divisão não pode ser feita.")

        print ()

    case 2:
        print("Média de 3 valores")
        primeiro_num = float (input("Digite o número 1: "))
        segundo_num = float (input("Digite o número 2: "))
        terceiro_num = float (input("Digite o número 3: "))
        
        soma = primeiro_num + segundo_num + terceiro_num
        media = soma/3

        print ("A média dos números é", media)
    case 3:
        print("Fórmula de Bháskara")