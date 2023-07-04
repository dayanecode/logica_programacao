
# Procedimento com parâmetro
def saudacao(hora):
    if hora < 12:
        mensagem = "Bom dia"
    elif hora < 18:
        mensagem = "Boa tarde"
    else: 
        mensagem = "Boa noite"
    print(mensagem, ", seja bem vindo à DLM!"  )
    

# Programa princiPAL
saudacao(int(input("Que horas são? ")))



