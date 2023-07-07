num = int(input("Digite 5 números. 1º: "))
menor = num


for cont in range (1, 5, 1):
    num = int(input(f"${cont+1}º: "))
    if num < menor:
        menor = num

print("O menor número é: ", menor)

     