from sistema import *
import os 

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def letreiro():
 
    banner = """
    
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║                                                                           ║
    ║   ██████╗  ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ ███╗██╗ █████╗ ███╗   ██╗ ║
    ║  ██╔════╝  ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔╝██║██╔══██╗████╗  ██║ ║
    ║  ██║  ███╗ ██║   ██║███████║██████╔╝██║  ██║██║██║ ██║███████║██╔██╗ ██║ ║
    ║  ██║   ██║ ██║   ██║██╔══██║██╔══██╗██║  ██║██║██║ ██║██╔══██║██║╚██╗██║ ║
    ║  ╚██████╔╝ ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ██║██║  ██║██║ ╚████║ ║
    ║   ╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ║
    ║                                                                           ║
    ║   ███████╗████████╗ ██████╗  ██████╗██╗  ██╗                              ║
    ║   ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝                              ║
    ║   ███████╗   ██║   ██║   ██║██║     █████╔╝                               ║
    ║   ╚════██║   ██║   ██║   ██║██║     ██╔═██╗                               ║
    ║   ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗                              ║
    ║   ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝                              ║
    ║                                                                          ║
    ║           🔒 SISTEMA DE GESTÃO SEGURA 🔒                                    ║
    ║                                                                           ║
    ╚════════════════════════════════════════════════════════════════════════════╝
    
    """
    print(banner)

def menu_principal():
    
    x = int(input('''O que você gostaria de fazer?
    (1) Logar
    (2) Registrar
    (3) Gerenciar cadastros
    '''))

    while True:
        if x == 1:
            LimpaTela()
            login()
            
            break
        elif x == 2:
            LimpaTela()
            cria_usuario()
            break
        elif x == 3:
            LimpaTela()
            gerenciar()
            break
        else:
            print("Entrada invalida! Digite novamente: ")
            x = int(input())
    

#<<<<<<< HEAD


#=======
def menu_inventario():
    x = int(input('''O que você gostaria de fazer?
    (1) cadastrar produto
    (2) apagar produto
    (3) consultar
    '''))

    while True:
        if x == 1:
            ad_inventario(d_inventario, chave)
            break
        elif x == 2:
            apaga_iten()
            break
        elif x == 3:
            
            break
        else:
            print("Entrada invalida! Digite novamente: ")
            x = int(input())

letreiro()

menu_principal()

LimpaTela()

#>>>>>>> 2b4d7a8 (10-06)
menu_inventario()
