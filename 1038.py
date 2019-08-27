entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])

if codigo == 1:
    valor = 4.00
elif codigo == 2:
    valor = 4.50
elif codigo == 3:
    valor = 5.00
elif codigo == 4:
    valor = 2.00
else:
    valor = 1.50
valor = float(valor)
total = valor * quantidade
print('Total: R$ %.2f' % total)
