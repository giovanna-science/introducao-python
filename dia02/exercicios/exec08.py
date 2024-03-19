# %%
 #dicionario onde cada item é uma chave e o valor corresp é o preco do item
precos = {
"casquinha" : 1.00,
"cascao" : 2.50,
"cestinha" : 4.00,
"caramelo" : 1.50,
"morango" : 1.50,
"chocolate" : 1.50,
"sem cobertura" : 1.50
}

#o metodo lower() converte o dado inserido em letras minusculas de acordo com as chaves do dict
tipo = input("Bem vindo a Sorveteria! \nDigite a opção desejada. \nCasquinha (R$1.00) \nCascão (R$2.50) \nCestinha (R$4.00)\n").lower()
sabor = input("Qual será o sabor do seu sorvete? \n Digite a opção desejada. \nMorango \nCreme \nChocolate\n").lower()
cobertura = input("E a cobertura? \n Digite a opção desejada. \nCaramelo (R$1.50) \nMorango (R$1.50) \nChocolate (R$1.50) \nSem cobertura (R$0,00)\n").lower()
#Na variavel valor, acesso o preco do tipo, sabor e cobertura escolhido pelo usuário e somo
valor = precos[tipo] + precos[sabor] + precos[cobertura]

print("Seu sorvete", tipo, "sabor", sabor, "com cobertura de", cobertura, "custa R${:.2f}".format(valor))







