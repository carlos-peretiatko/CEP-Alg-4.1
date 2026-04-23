# Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
# número inteiro positivo fornecido pelo usuário.

# Entrada do usuário
N = int(input("Digite um número inteiro positivo: "))

# Inicialização da soma
A = 0

# Cálculo da soma
for i in range(1, 2 * N, 2):
    A += 1 / i

# Resultado
print(f"O valor de A é: {A}")