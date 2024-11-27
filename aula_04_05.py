#
for i in range(10):
    nome = input("iNFORME O NOME DO ESTUDANTE: ")
    nota1 = float(input("INFORME A PRIMEIRA NOTA: "))
    nota2 = float(input("INFORME A SEGUNDA NOTA: "))
    media = (nota1 + nota2) / 2
    if media >= 70:
        print(f"{nome}, você está APROVADO")
    elif media >= 30:
        print(f"{nome}, você está em RECUPERAÇÃO")
    else:
        print(f"{nome}, você está REPROVADO")