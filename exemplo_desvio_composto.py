# 	Escreva “Digite o seu tempo de casa: ”
# Leia tempo
tempo = int(input("Digite o tempo de casa: "))
# Escreva “Digite o seu salário: R$ “
# Leia salario
salario = float(input("Digite o salário: R$ "))

if tempo < 3:
    aumento = salario * 5 / 100
else:
    aumento = salario * 10 / 100
novo_salario = salario + aumento
print("O seu salário foi de R$ ", salario, " para R$ ", novo_salario)