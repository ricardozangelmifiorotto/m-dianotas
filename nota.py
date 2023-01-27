#lista de média de notas
medias = []
#lista de semestres
semestres = []

while True:
    #lista de notas
    notas = []
    # Adicionar nome do semestre
    semestre = input("Digite o nome do semestre ou 'q' para sair: ")
    if semestre == 'q':
        break
    else:
        semestres.append(semestre)
        # Adicionar nome da matéria
        while True:
            materia = input("Digite o nome da matéria ou 'q' para sair: ")
            if materia == 'q':
                break
            else:
                # adicionar notas
                while True:
                    nota = input("Digite uma nota ou 'q' para sair: ")
                    if nota == 'q':
                        break
                    else:
                        notas.append(float(nota))
                soma = sum(notas)
                num_notas = len(notas)
                media = soma / num_notas
                medias.append((semestre, materia, media))

#calcula a média geral entre semestres
soma_geral = 0
num_medias = 0
for semestre, materia, media in medias:
    soma_geral += media
    num_medias += 1

media_geral = soma_geral/num_medias

#imprime as médias de cada matéria
print("Médias por semestre: ")
for semestre, materia, media in medias:
    print("A média de notas em", materia, "no semestre", semestre, "é:", media)

print("\nMédia geral entre os semestres: ", media_geral)

#calcula a média por matéria digitada
materia_escolhida = input("Digite o nome da matéria para calcular a média: ")
soma_materia = 0
num_materia = 0
for semestre, materia, media in medias:
    if materia == materia_escolhida:
        soma_materia += media
        num_materia += 1

media_materia = soma_materia/num_materia

print("\nMédia em", materia_escolhida, "entre os semestres: ", media_materia)
