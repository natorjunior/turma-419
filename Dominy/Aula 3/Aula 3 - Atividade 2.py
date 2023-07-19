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

dicionario = {"Aluno:":aluno,
              "Notas:":notas,
              "Maior nota:": max(notas),
              "Menor nota:": min(notas),
              "Média:": sum(notas)/len(notas),
              "Situação:": situacao}

for chave, valor in dicionario.items():
    print(chave,valor)
