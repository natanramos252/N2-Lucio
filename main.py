from sistema import *
import os 

##def LimpaTela():
##    os.system('cls' if os.name == 'nt' else 'clear')

def letreiro():
 
    banner = """
    
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║                                                                           ║
    ║   ██████╗  ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ ███╗██╗ █████╗ ███╗   ██╗ ║
    ║  ██╔════╝  ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔╝██║██╔══██╗████╗  ██║  ║
    ║  ██║  ███╗ ██║   ██║███████║██████╔╝██║  ██║██║██║ ██║███████║██╔██╗ ██║  ║
    ║  ██║   ██║ ██║   ██║██╔══██║██╔══██╗██║  ██║██║██║ ██║██╔══██║██║╚██╗██║  ║
    ║  ╚██████╔╝ ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ██║██║  ██║██║ ╚████║  ║
    ║   ╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ║
    ║                                                                           ║
    ║   ███████╗████████╗ ██████╗  ██████╗██╗  ██╗                              ║
    ║   ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝                              ║
    ║   ███████╗   ██║   ██║   ██║██║     █████╔╝                               ║
    ║   ╚════██║   ██║   ██║   ██║██║     ██╔═██╗                               ║
    ║   ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗                              ║
    ║   ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝                              ║
    ║                                                                           ║
    ║           🔒 SISTEMA DE GESTÃO SEGURA 🔒                                  ║
    ║                                                                            ║
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
    

letreiro()

if menu_principal():
    LimpaTela()
    menu_inventario()

else:
    menu_principal()
