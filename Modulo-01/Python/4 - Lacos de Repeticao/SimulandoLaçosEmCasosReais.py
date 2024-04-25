# DESENVOLVER ALGORITMO
# Diretor cadstra alunos com os dados:
# -Nome, cpf, Email, Matricula.
# pra cada aluno cadastrado, o diretor pode lançar 3 notas
# Se a média atingida for maior ou igual a 6, escrever:
# Aluno X, você foi aprovado. Seu diploma terá os seguintes dados:
# listar todos os dados daquele aluno
# caso a média seja inferior a 6, lançar uma nota adicional
# e tirar a média novamente
# senão , aluno reprovado.

class Aluno:
    def __init__(self, nome, cpf, email, matricula):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


def imprimir_dados_aluno(aluno):
    print("\nDados do aluno:")
    print(f"Nome: {aluno.nome}")
    print(f"CPF: {aluno.cpf}")
    print(f"Email: {aluno.email}")
    print(f"Matrícula: {aluno.matricula}")
    print(f"Notas: {aluno.notas}")
    print(f"Média: {aluno.calcular_media()}")


def main():
    alunos = []

    while True:
        print("\n1. Cadastrar aluno")
        print("2. Lançar notas")
        print("3. Imprimir dados de aluno")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome do aluno: ")
            cpf = input("CPF do aluno: ")
            email = input("Email do aluno: ")
            matricula = input("Matrícula do aluno: ")
            alunos.append(Aluno(nome, cpf, email, matricula))
        elif opcao == 2:
            matricula = input("Matrícula do aluno: ")
            aluno_encontrado = None
            for aluno in alunos:
                if aluno.matricula == matricula:
                    aluno_encontrado = aluno
                    break

            if aluno_encontrado:
                for _ in range(3):
                    nota = float(input(f"Nota {_ + 1} do aluno: "))
                    aluno_encontrado.adicionar_nota(nota)
                media = aluno_encontrado.calcular_media()
                if media >= 6:
                    print(f"Aluno {aluno_encontrado.nome}, você foi aprovado!")
                    imprimir_dados_aluno(aluno_encontrado)
                else:
                    print("Média insuficiente. Lançando nota adicional.")
                    nota_adicional = float(input("Nota adicional: "))
                    aluno_encontrado.adicionar_nota(nota_adicional)
                    nova_media = aluno_encontrado.calcular_media()
                    if nova_media >= 6:
                        print("Aluno ", {aluno_encontrado.nome})
                        print("você foi aprovado!")
                        imprimir_dados_aluno(aluno_encontrado)
                    else:
                        print("Aluno ", {aluno_encontrado.nome})
                        print("você foi reprovado.")
            else:
                print("Aluno não encontrado.")
        elif opcao == 3:
            matricula = input("Matrícula do aluno: ")
            aluno_encontrado = None
            for aluno in alunos:
                if aluno.matricula == matricula:
                    aluno_encontrado = aluno
                    break

            if aluno_encontrado:
                imprimir_dados_aluno(aluno_encontrado)
            else:
                print("Aluno não encontrado.")
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
