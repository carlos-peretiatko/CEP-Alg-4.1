# Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
# número inteiro positivo fornecido pelo usuário.

#A = N + N-1/2 + N-2/3 + ... + 1/N

n = int(input("Informe o número para realizar a conta: "))

A = 0

for i in range(1, n + 1):
    A += (n - i + 1) / i
    
print("O valor de A é: ", A)