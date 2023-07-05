# Função que verifica se a nota é valida
def notaValida(nota):
    if (nota >= 0 and nota <= 10 ):
        return True
    
# Programa principal
nota1 = float(input("Digite a primeira nota: "))
if (notaValida(nota1)):
   nota2 = float(input("Digite a segunda nota: "))
   if (notaValida(nota2)):
      media = (nota1 + nota2) / 2
      print(f"A média de {nota1} com {nota2} é {media}.")
   else: 
       print(f"A nota 2 ({nota2}) é inválida. Digite uma nota válida!")
else:
    print(f"A nota 1 ({nota1}) é inválida. Digite uma nota válida!")




    

