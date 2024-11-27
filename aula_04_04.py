soma = 0
media = 0
num_maior = 0
nome_maior = ""
for i in range(3):
    nome = input("Nome: ")
    num = int(input("Informe a idade: "))
    if num > num_maior:
        num_maior = num
        nome_maior = nome
    soma = soma + num
media = soma / (i + 1)
print(f"O resultado da soma de idades é: {soma} anos e a média de idades é: {media} anos e a pessoa mais velha é {nome}")