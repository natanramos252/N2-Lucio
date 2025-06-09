from sistema import *
import os 

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
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


def menu_inventario():
    x = int(input('''O que você gostaria de fazer?
    (1) cadastrar produto
    (2) apagar produto
    (3) consultar
    '''))

    while True:
        if x == 1:
            ad_inventario()
            break
        elif x == 2:
            apaga_iten()
            break
        elif x == 3:
            
            break
        else:
            print("Entrada invalida! Digite novamente: ")
            x = int(input())

menu_principal()

#if logar():

menu_inventario()
