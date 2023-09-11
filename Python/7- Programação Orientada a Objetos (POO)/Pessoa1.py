class Pessoa1:
    nome = "Marcio"
    idade = 38


""" # método = função
    def exibir(self, nome, idade):
        print(nome, idade) """

# método construtor


def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    print(self.nome, self.idade)
