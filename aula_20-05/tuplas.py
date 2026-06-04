# Um vetor é uma variável que recebe diversos valores, em posições diferentes
alunos = ["Davi","Daniel","Wanchise","Igor","Nicoli","Ian","Natasha","Fabio","Antoni"]
print("Formação original")
print(alunos[0])
# Para adiconar um valor ao final da lista, usamos a função append()
alunos.append("Antoni")
print("Adicionamos o Antoni")
# Para remover um valor, usamos a função remove()
alunos.remove("Nicoli")
print("Removemos a Nicoli")
print()
# Usamos a função len() para verificar a quantidade de itens em um vetor
print(f"Há {len(alunos)} alunos presente hoje!")
print()
# Para iterar entre os itens do vetor, podemos usar a função
# for  <variável item> in <variável vetor>:
for aluno in alunos:
    print(f"Boa Noite {aluno}")