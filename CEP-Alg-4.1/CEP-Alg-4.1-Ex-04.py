# Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
# número inteiro positivo fornecido pelo usuário.

#A = 1 + 1/2 + 1/3 + ... 1/n

A = int(input("Informe um número para fazer a conta: "))

for i in range(1, A + 1):
    A += 1 / i
    
print("A vale: ", A)