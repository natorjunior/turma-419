notas = []
aluno = input("Qual o seu nome? ")
for alunos in range(4):
    valor = int(input("Digite sua nota: "))
    notas.append(valor)
media = sum(notas)/len(notas)

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

dicionario = {"Aluno":aluno,
              "Notas":notas,
              "Maior_nota": max(notas),
              "Menor_nota": min(notas),
              "Média": sum(notas)/len(notas),
              "Situação": situacao}

print(dicionario)