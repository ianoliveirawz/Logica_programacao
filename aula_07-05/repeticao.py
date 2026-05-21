import time
import random

print ("#### Jogo da adivinhação ####")
print ()
print ("Estou pensando em um número...")
time.sleep(2)
numero = random.randint(0,10)
print("Pensei!")
print ("Você poderá tentar adivinhar ele")
print ()
# * para i em um intervalo de 1 até 4
#for i in range(1,4):
#    print (f"Essa é a sua {i} tentativa!")
#    tentativa = int (input("Digite um valor entre 0 e 10:"))
#    if tentativa == numero:
#            print ("Parabéns, você acertou!")
#    else:
#            print ("Você errou!")
acertou = False
num_tentativa = 0
while acertou == False:
    num_tentativa += 1 #mesma coisa que num_tentativa = num_tentativa + 1
    print (f"Essa é a {num_tentativa}ª tentativa")
    tentativa = int(input("Digite um valor entre 0 e 10: "))
    if tentativa == numero:
        print("Parabéns, você acertou!")
        acertou = True
    else:
        print("Você errou")
        if num_tentativa == 10:
            print ("Seu idiota, você é burro animal")