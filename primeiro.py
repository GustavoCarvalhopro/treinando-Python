a =int (input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O primeiro é o maior número valendo {}'.format(a))
elif b > a and b > c:
    print('O segundo é o maior número valendo: {}' .format(b))
else:
    print('O terceiro é o  maior número valendo: {}'.format(c))                
print('Final do Programa')    