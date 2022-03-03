print('='*40)
print(f'{"CONVERSOR" :^40}')
print('='*40)
num = -1
while True:
    num = int(input('Digite um numero inteiro qualquer: '))
    print('''Escolha umas das bases para conversão:'
    [1] converter para BINARIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL
    [0] SAIR ''')
    opção = int(input('Sua opção :'))
    print('=' * 40)
    if opção == 1:
        print('{} convertido para BINARIO é igual a {}'.format(num,bin(num)[2:]))
    elif opção == 2 :
        print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
    elif opção == 3:
        print('{} covertido para hexadecimal é igual a {}'.format(num,hex(num)[2:]))
    elif opção == 0:
        print('Finalizando! Obrigado por usar o Conversor')
        break
    else:
        print('Opção invalida TENTE NOVAMENTE')