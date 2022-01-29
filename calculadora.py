
while True:
    try:
        # Pergunta se a pessoa quer calcular.
        pergunta = input('Você quer calcular (s,n)? ').lower()

        # Verifica se a pessoa não quer calcular.
        if pergunta == 'n':
            break

        # Verifica se a pessoa digitou apenas "S" ou "N"
        if not pergunta == 's' or pergunta == 'n': 
            print('Digite apenas "S" ou "N"')
            continue

        # Pega os números e o operador.
        num1 = float(input('Digite um número: '))
        op = input('Digite o operador: ')
        num2 = float(input('Digite outro número: '))

        # Lista dos operadores disponiveis.
        operadores = ('+', '-', '*', '/')

        # Verifica se o operador digitado existe na lista.
        if not op in operadores:
            print(f'"{op}" operador inválido.')
            continue

        # Função de somar.
        if op == '+': resultado = lambda n1, n2: n1 + n2

        # Função de subtrair.
        elif op == '-': resultado = lambda n1, n2: n1 - n2

        # função de multiplicar.
        elif op == '*': resultado = lambda n1, n2: n1 * n2

        # Função de dividir.
        elif op == '/': resultado = lambda n1, n2: n1 / n2

        # Chama a função lambda.
        resultado = resultado(num1, num2)

        # Exibe na tela o resultado.
        print(f'Resultado = {resultado}')

    # Verifica se não foi possivel tranformar a string em float.
    except ValueError:
        print('Digite apenas números.')