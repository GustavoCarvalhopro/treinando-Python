a = int(input('Entre com a nota do primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou uma nota errada. Digite a nota do primeiro bimestre: '))

b = int (input('Entre com a nota do segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou uma nota errada. Entre com a nota do segundo bimestre: '))

c = int (input('Entre com a nota do terceiro bimestre: '))
while c > 10:
    c = int (input('Você digitou uma nota errada. Entre com a nota do terceiro bimestre: '))

d = int (input('Entre com a nota do quarto bimestre: '))
while d > 10:
    d = int (input('Você digitou uma nota errada. Entre com a nota do quarto bimestre: '))

nota = (a + b + c + d) / 4

if nota >= 7:
    print('Parabéns você foi aprovado com a nota: {} de 10.'.format(nota))

elif nota >= 5:
    print('Vamos te dar mais uma chance procure a direção para marcar sua recuperação. Sua nota foi: {} de 10.'.format(nota))

else:
    print('Você foi reprovado.... Sua nota foi: {} de 10.'.format(nota))
