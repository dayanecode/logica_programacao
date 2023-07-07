# Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

# função que verifica se a nota é válida
def notaValida(nota):
    if (nota >= 0 and nota <= 10):
        return True

lista = []

# armazena 4 notas dentro da lista
for cont in range(1, 5, 1):
    notaDigitada = float(input("Digite uma nota: "))

    # Enquanto a nota digitada não for válida
    while notaValida(notaDigitada) != True:
        # Imprima esta mensagem
        print("Digite uma nota válida!")
        # Peça para o usuário digitar novamente:
        notaDigitada = float(input("Digite uma nota: "))
    # Se a nota digitada for válida, adiciona a nota digitada à lista
    lista.append(notaDigitada)

print(lista)

# calcula média final
mediaFinal = sum(lista)  / len(lista)

# calcula maior elemento 
maiorNota = max(lista)

# calcula menor elemento
menorNota = min(lista)

print(f"A média final é igual a {mediaFinal:.2f}.\nA maior nota da lista é {maiorNota}.\nA menor nota da lista é {menorNota}.")