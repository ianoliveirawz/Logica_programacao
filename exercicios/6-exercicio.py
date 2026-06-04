alunos = []

for i in range(0,3):
    print(f"=============== ALUNO {i+1} ===============")
    nome = input("Digite o nome do aluno: ")
    aluno = {
        "nome":nome,
        "notas":[],
        "media":0
    }
    for j in range(0,4):
        print(f"Digite a nota {j+1}")
        nota = float(input("Nota:"))
        aluno["notas"].append(nota)

    aluno["media"] = (aluno["notas"][0]+aluno["notas"][1]+aluno["notas"][2]+aluno["notas"][3])/4

    alunos.append(aluno)
    print()

print(alunos)