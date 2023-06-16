
venda = float(input("Digite o valor da venda: R$ "))

if venda > 300:
    desconto = venda * 10 / 100
    venda = venda - desconto

print("Valor final: R$ ", venda)
