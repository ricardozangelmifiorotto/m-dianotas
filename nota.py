# lista de notas
notas = []

# adicionar notas
while True:
    nota = input("Digite uma nota ou 'q' para sair: ")
    if nota == 'q':
        break
    else:
        notas.append(float(nota))

# calcula a média
soma = sum(notas)
num_notas = len(notas)
media = soma / num_notas

# imprime a média
print("A média de notas é:", media)
