# %%

nome = input("Olá. Qual o seu nome?")

#a funcao any retorna true (valida a instrucao)
#o metodo split() divide a string de nome(variavel) 
#usando o espaço como delimitador das palavras
if any("calvo" in parte.lower() for parte in nome.split()):
    print(nome, "você pertence à família Calvo.")
else:
    print(nome, "você não pertence à família Calvo.")

