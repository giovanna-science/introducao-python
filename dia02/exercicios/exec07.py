# %%

agua_natural = 1.50
agua_gas = 2.50


escolha = input("Bem vindo a Distribuidora de Água. \nQual o seu pedido? \nDigite 1 para Água Mineral Natural ou 2 para Água Mineral com Gás")
qnt = float (input("\nQuantas unidades?"))

#a função format() formata strings e dentro de {} 
# é possível armazenar variaveis nmrs ou expressões
if escolha == "1":
    #"{:.2f}" formata um nmr de ponto flutuante (f) com duas casas decimais (.2)
    print("Seu pedido custa", "{:.2f}".format(agua_natural * qnt))
elif escolha == "2":
    print("Seu pedido custa", "{:.2f}".format(agua_gas * qnt))
    