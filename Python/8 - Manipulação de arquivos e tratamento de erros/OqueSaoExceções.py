""" a = int(input("Digite um Numero = "))
b = int(input("Digite um Outro Numero = "))

resultado = a / b

print(resultado) """

# divide 4 por 0 vai dar erro!

# ajustando o tratamento do erro

try:
    a = int(input("Digite um Numero = "))
    b = int(input("Digite um Outro Numero = "))

    resultado = a / b

    print(resultado)

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")
except ValueError:
    print("Erro: Certifique-se de digitar números válidos.")
