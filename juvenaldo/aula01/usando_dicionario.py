notas = []
nomeEstudante = input("Digite o seu nome: ")
for i in range (0,4):
    nota=int(input("Digite notas: "))
    notas.append(nota)
media = sum(notas)/len(notas)
print(media)

maiorNota = max(notas)
menorNota = min(notas)

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

dicionarioVariavel = {
    "nomeEstudante": nomeEstudante,
    "maiorNota": maiorNota,
    "menorNota": menorNota,
    "media": media,
    "situação": situacao

}

print(dicionarioVariavel)