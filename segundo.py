a = int (input('Entre com um valor: '))
for i in range (a):

    div = 0
    for x in range(1, i+1):
        resto = i % x
        if resto == 0:
            div = div + 1

    if div == 2:
        print('Número {} é primo' .format(i))
