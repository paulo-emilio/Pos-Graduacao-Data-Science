# print(soma(9, 8, 8))

# fatorial

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)


print(fatorial(5))
