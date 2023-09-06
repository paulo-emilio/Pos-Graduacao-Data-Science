# para quando tem somente um processador, tudo bem assim:

a = 1
b = 2
c = 3
d = 4

soma = a + b + c + d
print(soma)

# para quando temos vários processadores, podemos dividir as tarefas entre eles:

a = 1
b = 2
c = 3
d = 4

e = a + b
f = c + d

soma = e + f
print(soma)
