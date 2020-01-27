while True:

    operaçao = input('selecione uma operaçao ou aperte x para sair')
    if operaçao == 'x' or operaçao == 'X':
        break

    if operaçao == '+' or operaçao == '-' or operaçao == '*' or operaçao == '/':
        n1 = int(input('Digite o primeiro numero'))
        n2 = int(input('Digite o segundo numero'))

    else: print('operaçao inválida')

    if operaçao == '+':
        result = n1 + n2
        print(result)

    elif operaçao == '-':
        result = n1-n2
        print(result)

    elif operaçao == '*':
        result = n1 * n2
        print(result)
        
    elif operaçao == '/':
        result = n1/n2
        print(result)
