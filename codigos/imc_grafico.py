# Importacao das bibliotecas

import tkinter as tk
from tkinter import ttk

# Definição da declaração das variaveis e das entradas dos dados

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def exibir_classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"
    
def cadastrar_pessoa():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())

    imc = calcular_imc(peso, altura)
    classificacao = exibir_classificacao_imc(imc)

# Exibe o resultado das variaveis digitadas nos widgets

    resultado_label.config(text=f" Nome: {nome} \n Idade: {idade} anos \n Peso: {peso} kg"
                                f"\n Altura: {altura} m \n IMC : {imc:.2f}")
    classificacao_label.config(text=f"A classificação é: {classificacao}")

# Cria a janela principal

root = tk.Tk()
root.geometry("300x400")
root.title("Calculadora de IMC")
root.configure(bg="blue")
fonte = ("Arial", 10)

# Cria os widgets(Botoes)
nome_label = ttk.Label(root, text="Nome:")
nome_entry = ttk.Entry(root)

idade_label = ttk.Label(root, text="Idade(anos):")
idade_entry = ttk.Entry(root)

peso_label = ttk.Label(root, text="Peso(kg):")
peso_entry = ttk.Entry(root)

altura_label = ttk.Label(root, text="Altura(m):")
altura_entry = ttk.Entry(root)

calcular_button = ttk.Button(root, text="Calcular IMC", command=cadastrar_pessoa)

resultado_label = ttk.Label(root, text="")
classificacao_label = ttk.Label(root, text="")

# Posiciona os widgets na janela(Local pra digitar os dados)
nome_label.grid(row=0, column=0, padx=10, pady=5)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

idade_label.grid(row=1, column=0, padx=10, pady=5)
idade_entry.grid(row=1, column=1, padx=10, pady=5)

peso_label.grid(row=2, column=0, padx=10, pady=5)
peso_entry.grid(row=2, column=1, padx=10, pady=5)

altura_label.grid(row=3, column=0, padx=10, pady=5)
altura_entry.grid(row=3, column=1, padx=10, pady=5)

calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

resultado_label.grid(row=5, column=0, columnspan=2, pady=5)
classificacao_label.grid(row=6, column=0, columnspan=2, pady=5)

# Inicia o loop principal da interface grafica

root.mainloop()