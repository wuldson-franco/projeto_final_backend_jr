
import tkinter as tk

# Função para criar o arquivo .txt
def criar_arquivo():
    with open("dados.txt", "w") as arquivo:
        arquivo.write("")

# Função para ler o arquivo .txt
def ler_arquivo():
    with open("dados.txt", "r") as arquivo:
        dados = arquivo.readlines()
    return dados

# Função para inserir um registro no arquivo .txt
def inserir_registro():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    sexo = entrada_sexo.get()
    matricula = entrada_matricula.get()
    nota1 = entrada_nota1.get()
    nota2 = entrada_nota2.get()
    nota3 = entrada_nota3.get()
    notas = [float(nota1) + float(nota2) + float(nota3)]
    media = sum(notas) / len(notas)
    dados = [nome, idade, sexo, matricula, nota1, nota2, nota3, media]
    with open("dados.txt", "a") as arquivo:
        arquivo.write("\n" + ",".join([str(elemento) for elemento in dados]))


# Função para excluir um registro no arquivo .txt
def excluir_registro():
    matricula = entrada_matricula.get()
    dados = ler_arquivo()
    for i in range(len(dados)):
        linha = dados[i].strip()
        if linha.startswith(matricula):
            del dados[i]
    with open("dados.txt", "w") as arquivo:
        arquivo.writelines(dados)

# Função para exibir os registros do arquivo .txt
def exibir_registros():
    dados = ler_arquivo()
    for linha in dados:
        linha = linha.strip()
        if linha:
            print(linha)

# Inicializando a interface gráfica
criar_arquivo()
janela = tk.Tk()
janela.title("CRUD Notas")
janela.geometry("300x400")

# Criando os campos de entrada
entrada_nome = tk.Entry(janela)
entrada_idade = tk.Entry(janela)
entrada_sexo = tk.Entry(janela)
entrada_matricula = tk.Entry(janela)
entrada_nota1 = tk.Entry(janela)
entrada_nota2 = tk.Entry(janela)
entrada_nota3 = tk.Entry(janela)

# Criando os botões
botao_criar = tk.Button(janela, text="Inserir", command=inserir_registro)
botao_ler = tk.Button(janela, text="Ler", command=exibir_registros)
botao_excluir = tk.Button(janela, text="Excluir", command=excluir_registro)

# Adicionando os campos de entrada e os botões à interface gráfica
entrada_nome.grid(row=0, column=0)
entrada_idade.grid(row=1, column=0)
entrada_sexo.grid(row=2, column=0)
entrada_matricula.grid(row=3, column=0)
entrada_nota1.grid(row=4, column=0)
entrada_nota2.grid(row=5, column=0)
entrada_nota3.grid(row=6, column=0)
botao_criar.grid(row=7, column=0)
botao_ler.grid(row=8, column=0)
botao_excluir.grid(row=10, column=0)

    # Chamando a função mainloop()
janela.mainloop()