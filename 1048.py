salario = float(input())
if 0 < salario <= 400.00:
    novoSalario = salario * 0.15
    reajusteGanho = salario + novoSalario
    percentual = 15
elif 400.01 <= salario <= 800.00:
    novoSalario = salario * 0.12
    reajusteGanho = salario + novoSalario
    percentual = 12
elif 800.01 <= salario <= 1200.00:
    novoSalario = salario * 0.10
    reajusteGanho = salario + novoSalario
    percentual = 10
elif 1200.01 <= salario <= 2000.00:
    novoSalario = salario * 0.07
    reajusteGanho = salario + novoSalario
    percentual= 7
elif 2000.00 < salario:
    novoSalario = salario * 0.04
    reajusteGanho = salario + novoSalario
    percentual= 4
print('Novo salario: %.2f' % reajusteGanho)
print('Reajuste ganho: %.2f' % novoSalario)
print('Em percentual: ', percentual, '%')
