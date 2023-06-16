
# •	Ler valor
valor = input("Digite um valor: R$ ")
valor = float(valor)

# •	Ler porcentagem
porcentagem = input("Digite a porcentagem: ")
porcentagem = float(porcentagem)

# •	Calcular percentual
percentual = valor * porcentagem / 100

# •	Calcular acréscimo
acrescimo = valor + percentual

# •	Calcular desconto
desconto = valor - percentual

# •	Exibir o percentual
print("O percentual é: R$ ", percentual)

# •	Exibir o acréscimo
print ("O valor com acréscimo é: R$ ", acrescimo)

# •	Exibir o desconto
print("O valor com desconto é: R$ ", desconto)