soma = 0
maior = 0
for i in range(5):
    num = int(input("Informe o Valor: "))
    if num > maior:
        maior = num
    soma = soma + num
print(f"O resultado da soma é: {soma} e o maior número informado é {maior}")