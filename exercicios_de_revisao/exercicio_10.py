import time
saldo = 1000
while True:
    print("=== CAIXA ELETRÔNICO ===")
    time.sleep(3)
    print("Bem vindo(a)!")
    time.sleep(2)
    print("1 - Verificar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    time.sleep(2)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print(f"Saldo atual: R$ {saldo}")
    elif opcao == 2:
        deposito = float(input("Valor para depósito em reais: "))
        saldo += deposito
        print("Depósito realizado com sucesso!")
        print(f"O saldo atual de sua conta está em R${saldo}")
    elif opcao == 3:
        saque = float(input("Valor para saque em reais: "))
        if saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso!")
            print(f"Seu saldo atual é de {saldo}")
        else:
            print("Saldo insuficiente!")
    elif opcao == 4:
        print("Sistema encerrado, até mais.")
        break
    else:
        print("Opção inválida!")