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
        return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


def leianome(msg):
    n = str(input(msg)).strip().title()
    return n
