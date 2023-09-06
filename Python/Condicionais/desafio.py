'''
Um algoritmo que:
peça ao usuário para digitar o seu ano de nascimento
descubra se ele é maior de idade
se for, peça o título de eleitor
se não, documento de um responsável
'''

from datetime import datetime

data_de_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")

data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")

data_atual = datetime.now()

idade = data_atual.year - data_de_nascimento.year

if (data_atual.month, data_atual.day) < (data_de_nascimento.month, data_de_nascimento.day):
    idade -= 1

int(input('Título de Eleitor: ')) if idade >= 18 else int(input('Documento de algum responsável: '))