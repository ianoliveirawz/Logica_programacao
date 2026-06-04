import time
print("=======================================================")
print("================= ¿ Par ou Ímpar ? ====================")
print("=======================================================")
time.sleep(2)
numero = int(input("Digite um número: "))
time.sleep(2)
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
print("=======================================================")