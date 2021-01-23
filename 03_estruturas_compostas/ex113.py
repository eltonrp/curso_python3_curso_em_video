def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!! Digite um número inteiro válido...\033[m')
            continue
        except (KeyboardInterrupt):
            print()
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        n = 0
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO!! Digite um número real válido...\033[m')
        except (KeyboardInterrupt):
            print()
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num2}')
