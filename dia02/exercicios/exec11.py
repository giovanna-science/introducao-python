# %%

lista = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']

compras = input("Qual item deseja comprar?").lower()

if compras not in lista:
    print("Seu item não está na lista.")
else:
    print("Seu item está na lista.")