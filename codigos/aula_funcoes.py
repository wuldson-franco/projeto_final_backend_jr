#%% -- Função Media
def media(lista):

  if len(lista) == 0:
    return None
  else:
    return sum(lista) / len(lista)

print(media([1, 2, 3, 4, 5]))
#%%

#%% -- Função IMC
def imc(peso, altura):
  """
  Calcula o Índice de Massa Corporal (IMC) de uma pessoa.

  Args:
    peso: O peso da pessoa em quilogramas.
    altura: A altura da pessoa em metros.

  Returns:
    O IMC da pessoa.
  """


  

  altura_quadrada = altura ** 2
  imc = peso / altura_quadrada
  return imc


if __name__ == "__main__":
  # Obtenha o peso e a altura da pessoa
  peso = float(input("Digite o peso (kg): "))
  altura = float(input("Digite a altura (m): "))

  # Calcule o IMC da pessoa
  imc = imc(peso, altura)

  # Imprima o IMC da pessoa
  print(f"O IMC da pessoa é {imc:.2f}.")
# %%