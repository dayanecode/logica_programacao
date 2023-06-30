# Dados dois números pelo usuário exibir os números do intervalo

# Exemplo de Laço FOR

ini = int(input("Digite o primeiro nº: "))
fim = int(input("Digite o último nº: "))


for cont in range (ini, fim + 1, 1):
    if cont > ini and cont < fim:
        print(f"for {cont}")

# Exemplo de Laço ENQUANTO FAÇA

while  ini < fim:
    print(f"while {ini}")
    ini = ini + 1 #para não dar laço infinito


# Exemplo de Laço DO WHILE
# Faça de qualquer forma

while True:
    print(f"laço do while {ini}")
    ini += 1
    if ini > fim:
        break





