# Desafio 1: 
'''
Uma função que:
peça ao usuário para digitar o seu ano de nascimento
descubra se ele é maior de idade
se for, peça o título de eleitor
se não, documento de um responsável
'''
from datetime import datetime

def maior_de_idade(data_de_nascimento):
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    data_atual = datetime.now()
    idade = data_atual.year - data_de_nascimento.year
    if (data_atual.month, data_atual.day) < (data_de_nascimento.month, data_de_nascimento.day):
        idade -= 1
    return int(input('Título de Eleitor: ')) if idade >= 18 else int(input('Documento de algum responsável: '))

maior_de_idade(input("Digite a data de nascimento (AAAA-MM-DD): "))


# Desafio 2: Contagem de 10 a 0 usando recursão:
def contar_dez_a_zero(n):
    if n >= 0:
        print(n)
        contar_dez_a_zero(n - 1)

# Chamando a função para iniciar a contagem
contar_dez_a_zero(10)
