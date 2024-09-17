n1 = (float(input('Digite o primeiro número: ')))
n2 = (float(input('Digite o segundo número: ')))


op = (int(input('[1] Somar \n[2] Subtrair \n[3] Multiplicar \n[4] Dividir \n[0] Sair \n')))

if op == 1:
    resultado = n1 + n2
    print(resultado)
elif op == 2:
    resultado = n1 - n2
    print(resultado)
elif op == 3:
    resultado = n1 * n2
    print(resultado)
elif op == 4:
    resultado = n1 / n2
    print(resultado)
else:
    print('DESLIGANDO')
