# Import
import random
from os import system, name

# Função para limpar a tela
def limpa_tela():

    #windows
    if name == 'nt':
        _ =  system('cls')
    #linux ou mac
    else:
        _ = system('clear')

#Criando o "boneco"
def display_hangman(chances):
    stages = [
        #estagio final
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -        
                """,
                # estagio 5
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -        
                """,
                #estagio 4
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -        
                """,
                # estagio 3
                """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -        
                """,
                # estagio 2
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -        
                """,
                # estagio 1
                """
                    --------
                    |      |
                    |      O
                    |      
                    |      
                    |     
                    -        
                """,
                # estagio 0
                """
                    --------
                    |      |
                    |      
                    |     
                    |     
                    |     
                    -        
                """        
    ]
    return stages[chances]

# Função conteudo
def game():

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra:\n')

    #lista palavras
    palavra = ['banana', 'maçã', 'granola', 'pasta de amendoin', 'whey']

    #usando a func random
    palavra = random.choice(palavra)

    lista_letras_palavras = [letra for letra in palavra]
    tabuleiro = ["_"] * len(palavra)
    chances = 6
    letras_tentativas = []

    while chances > 0:
        print(display_hangman(chances))
        print("\nPalavra: ", tabuleiro)
        print("\n")

        tentativa = input('\nDigite uma letra: ')
        
        if tentativa in letras_tentativas:
            print("Voce já usou essa, MANDA OUTRA.")
            continue

        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:
            print("Voce acertou a letra!")
            
            for indice in range(len(lista_letras_palavras)):

                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            
            if "_" not in tabuleiro:
                print("\nVocê venceu, a palavra era: {}".format(palavra))
                break
        else:
            print("OPS. TA ERRADO")
            chances -= 1

        # condicional
    if "_" in tabuleiro:
        print("\nVoce perdeu, a palavra era: {}.".format(palavra))


if __name__ == "__main__":
    game()
    print("\nParabens. voce esta aprendendo.\n")
