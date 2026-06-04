import time
import random
print("====================================================================")
print("Olá, Bem Vindo ao radar de velocidade!")
time.sleep(3)
print("Verificando a velocidade que seu carro percorreu . . .")
time.sleep(3)
velocidade = random.choice(range(1, 301))
if velocidade >= 30 and velocidade <= 80:
    print(f"Você está a {velocidade} km/h, está dentro do limite, continue assim!")
elif velocidade > 80 :
    print(f"Você está a {velocidade} km/h, você ultrapassou o limite de velocidade, tome cuidado!")