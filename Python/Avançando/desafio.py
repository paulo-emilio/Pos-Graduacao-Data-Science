# criar uma função para verificar se o valor "Loki" está presente na lista ou não
# se sim, exibi-lo, se não, exibir todos

lista = []

for a in range(5):
    lista.append(input('Nome: '))

def verificacao(lista):
    if "Loki" in lista:
        print('Loki')
    else:
        print(lista)

verificacao(lista)

