print ("Bem Vindo ao validador de CPF")
print()
cpf = input("Digite o seu CPF: ")
cpf.replace (".","")
cpf.replace ("-","")
cpf.strip()
caracteres_cpf = list(cpf)
decimo_caractere = 0
decimo_p_caractere = 0
soma = 0
soma = int(caracteres_cpf[0]) * 10
soma = soma + int(caracteres_cpf[1]) * 9
soma = soma + int(caracteres_cpf[2]) * 8
soma = soma + int(caracteres_cpf[3]) * 7
soma = soma + int(caracteres_cpf[4]) * 6
soma = soma + int(caracteres_cpf[5]) * 5
soma = soma + int(caracteres_cpf[6]) * 4
soma = soma + int(caracteres_cpf[7]) * 3
soma = soma + int(caracteres_cpf[8]) * 2
resto = soma % 11
if resto < 2:
    decimo_caractere = 0
else:
    decimo_caractere = 11 - resto
if decimo_caractere != int(caracteres_cpf[9]):
    print("O CPF é inválido")
else: 
    print("O décimo caractere bateu")