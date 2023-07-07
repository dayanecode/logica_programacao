soma = 0

# Faça
while True:
    # Peça um número
    num = int(input("Digite um número: "))
    # Verifique se o número é maior do que 10
    if (num >= 10):
        # Se for verdade adicione o número digitato a soma
        soma = soma + num
    # se não for verdade
    else:
        # o break vai forçar a saída do laço
        break
# E ao sair do laço mandamos exibir a somatória
print("A soma total dos números válidos informados é: ", soma)