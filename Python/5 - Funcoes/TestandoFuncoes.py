# Desafio 1 : Fazer o sistema de verificação de maioridade
# usando funções


def verificar_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False


def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if verificar_maioridade(idade):
        print(f"{nome}, você é maior de idade.")
    else:
        print(f"{nome}, você não é maior de idade.")


if __name__ == "__main__":
    main()

# Desafio 2: Fazer uma contagem de 0 a 10 recursão
# Fazer a mesma contagem de 10 a 0


def contagem_de_0_a_10(numero):
    if numero <= 10:
        print(numero)
        contagem_de_0_a_10(numero + 1)


def contagem_de_10_a_0(numero):
    if numero >= 0:
        print(numero)
        contagem_de_10_a_0(numero - 1)


print("Contagem de 0 a 10:")
contagem_de_0_a_10(0)

print("\nContagem de 10 a 0:")
contagem_de_10_a_0(10)
