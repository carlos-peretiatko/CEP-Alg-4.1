# 11. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
# número inteiro positivo fornecido pelo usuário.

# Entrada do usuário
N = int(input("Digite um número inteiro positivo: "))

A = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        A -= 1 / i  # termo par (negativo)
    else:
        A += 1 / i  # termo ímpar (positivo)

print(f"O valor de A é: {A}")