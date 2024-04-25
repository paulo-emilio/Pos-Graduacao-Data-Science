def soma(a, b, d):
    c = a + b + d
    if c % 2 == 0:
        return "par"
    else:
        return "Impar"


print(soma(4, 2, 10))
print(soma(0, 2, 4))
print(soma(2, 3, 1))
print(soma(9, 8, 8))
