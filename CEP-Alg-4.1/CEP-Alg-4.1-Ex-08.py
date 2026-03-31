# 8. Faça um programa Python que peça 10 números inteiros e apresente: a média, o maior e o
# menor dentre os 10 números fornecidos.

x = 0 #contador

i = []

while x != 10:
    numero = float(input(f"Digite o {x + 1} valor: "))
    i.append(numero)
    x += 1

# maior = max(i)
# menor = min(i)
# media = sum(i) / len(i)
print("Maior: ", max(i))
print("Menor: ", min(i))
print("Média: ", sum(i) / len(i))