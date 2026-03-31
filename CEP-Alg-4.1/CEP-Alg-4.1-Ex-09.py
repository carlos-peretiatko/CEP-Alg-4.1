# 9. Adapte seu programa da questão anterior para que ele receba uma quantidade indefinida de
# notas até que o usuário pressione <enter> sem fornecer nenhuma nota.

x = 0 #contador

i = []

while True:
    numero = input(f"Digite um valor: ")

    if numero == "":
        break
    
    numero = float(numero)
    i.append(numero)

# maior = max(i)
# menor = min(i)
# media = sum(i) / len(i)
if len(i) > 0:
    print("Maior:", max(i))
    print("Menor:", min(i))
    print("Média:", sum(i) / len(i))
else:
    print("Nenhum valor foi digitado.")
