#lista de média de notas
medias = []

while True:
    #lista de notas
    notas = []
    # Adicionar nome da matéria
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
        medias.append((materia,media))

#imprime as médias de cada matéria
for materia, media in medias:
    print("A média de notas em", materia, "é:", media)
