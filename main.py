from sistema import *

def menu_principal():
    
    x = int(input('''O que você gostaria de fazer?
    (1) Logar
    (2) Registrar
    (3) Gerenciar cadastros
    '''))

    while True:
        if x == 1:
            login()
            break
        elif x == 2:
            cria_usuario()
            break
        elif x == 3:
            gerenciar()
            break
        else:
            print("Entrada invalida! Digite novamente: ")
            x = int(input())


menu_principal()

menu_inventario()
