dicionario = {}
maiorNota = 0
nomeAluno = ""
for i in range (0,4):
    aluno1 = input("Nome: ")
    nota = float(input("Digite a nota: "))
    dicionario[aluno1]= nota
    if nota > maiorNota:
        maiorNota = nota
        nomeAluno = aluno1
notas = dicionario.values()
print("A media é igual a",sum(notas)/len(notas))
print(f"O aluno {nomeAluno}", maiorNota)
