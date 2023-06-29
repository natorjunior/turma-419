notas = []
for i in range (4):
    nota = float(input(f"Digite a nota {i+1}"))
    notas.append(nota)

media = sum(notas)/len(notas)
Nome = input("Digite o nome do aluno: ")
aluno = {
    'Nome': Nome,
    'Notas':notas,
    'Maior Nota': max(notas),
    'Menor Nota': min(notas),
    'Media':media,
    'Situação':'Aprovado' if media >=7 else 'Reprovado'
}
print("Informações do aluno")