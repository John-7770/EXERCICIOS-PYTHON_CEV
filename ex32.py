ano = int(input('Digite um ano -> '))
print()
anoB = ano % 400
anoB1 = anoB in range(101 + 3, 197, 4)
anoB2 = anoB in range(201 + 3, 297, 4)
anoB3 = anoB in range(301 + 3, 397, 4)
if anoB in range(0, 97, 4):
    print(ano, 'É bissexto.')
elif anoB1:
    print(ano, 'É bissexto.')
elif anoB2:
    print(ano, 'É bissexto.')
elif anoB3:
    print(ano, 'É bissexto.')
else:
    print(ano, 'Não é bissexto.')