num = int(input('Digite um numeto inteiro: '))
print('''Escolha uma das bases para conversção
[ 1 ] converter para BINÁRIA
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua Opção: '))
if opçao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HETADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, Tente novamente! ')
