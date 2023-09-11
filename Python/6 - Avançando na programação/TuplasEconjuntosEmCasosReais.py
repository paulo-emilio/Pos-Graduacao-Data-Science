# desafio:
# criar uma função recursiva (ou não) para verificar se
# o valor "Descomplica está presente entre um dos nomes
# inseridos na lista
# se foi: Exibir apenas o nome DESCOMPLICA
# senão, exibir todos os nomes

""" lista = []

for a in range(5):
    lista.append(input("Nome: "))
print(lista)
 """

# resolução do desafio:


def verifica_descomplica(nomes, indice=0):
    if indice >= len(nomes):
        print("DESCOMPLICA não encontrado")
        return
    if nomes[indice].lower() == "descomplica":
        print("DESCOMPLICA encontrado!")
        return
    verifica_descomplica(nomes, indice + 1)


# Exemplo de nomes na lista
nomes = ["João", "Maria", "Pedro", "descomplica", "Ana"]
verifica_descomplica(nomes)
