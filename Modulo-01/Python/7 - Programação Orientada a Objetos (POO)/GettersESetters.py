from Pessoa1 import Pessoa1
pessoa = Pessoa1()

# GETTERS E SETTERS


@property
def nome(self):
    return self._nome


@nome.setter
def nome(self, nome):
    self._nome = nome
