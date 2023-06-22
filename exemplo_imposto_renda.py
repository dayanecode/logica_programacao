salario = float(input("Digite o salário: R$"))
if salario <= 1900:
	ir = 0
elif salario <= 2800:
	ir = salario * 0.15
else:
	ir = salario * 0.275
salario_liquido = salario - ir
print(f"O desconto do IR é de R$ {ir:.2f} e o salário líquido é igual a R$ {salario_liquido}" )    
