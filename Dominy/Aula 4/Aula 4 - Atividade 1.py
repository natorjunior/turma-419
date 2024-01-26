notas = []
aluno = []
while True:
    serie = int(input("Digite sua nota aqui: "))
    notas.append(serie)
    nome = input("Digite aqui o seu nome: ")
    aluno.append(nome)
    valor = int(input("Você deseja sair?\n"
                      "1 - Continuar\n"
                      "0 - Sair\n"))
    if valor == 0:
        dicionario = {"Alunos":[aluno,notas],
                      "Média = ": sum(notas)/len(notas),
                      "Maior nota = ": max(notas)}
        break
print(dicionario)
