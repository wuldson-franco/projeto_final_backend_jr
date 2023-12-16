#%%
# Criando um dicionário
dicionario = {"nome": "João", "idade": 30}
#%%
print(dicionario)

# %%
# Adicionando um elemento a um dicionário
dicionario["cidade"] = "João Pesoa"
# %%
# Removendo um elemento de um dicionário
del dicionario["idade"]

# %%
# Iterando sobre um dicionário
for valor in dicionario.values():
    print(f"Valor: {valor}")

#%%
for dado in dicionario:
    print(f'chave {dado} e o valor é {dicionario[dado]}')