# Um algoritmo que:
# peça ao usuário para digitar o seu ano de nascimento
# peça o anao atual
# descubra se o usuario é maior de idade
# se for,pede o titulo de eleitor dele
# senão, pede um documento do responsável.

anoNascimento = int(input("Digite seu ano de Nascimento = "))
anoAtual = int(input("Digite o ano Atual = "))
idade = anoAtual - anoNascimento

if idade >= 18:
    print("Digite o Titulo")
else:
    print("Digite documento de um responsável")
