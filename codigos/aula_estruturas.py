#%%
amigos = ["João", "Maria", "Pedro", "Ana"]

#%%
numero = int(input("Digite um número: "))

tabuada = {}
for i in range(1, 11):
    tabuada[i] = numero * i

print(f"A tabuada de {numero} é: {tabuada}")
# %%


# Criando uma lista para armazenar os usuários
usuarios = []

# Solicitando as informações do usuário
nome = input("Digite o nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))
email = input("Digite o email do usuário: ")

# Criando um dicionário para armazenar as informações do usuário
usuario = {"nome": nome, "idade": idade, "email": email}

# Adicionando o usuário à lista
usuarios.append(usuario)

# Imprimindo a lista de usuários
for usuario in usuarios:
    print(usuario)
# %%
