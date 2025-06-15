from sistema import (
    limpa_tela, cabecalho,
    login, cria_usuario, gerenciar_usuarios,
    CriptografiaInventario,
    le_inventario, gerenciar_inventario
)

def main():
    chave = input("Chave de criptografia (mín. 4 caracteres): ").strip()
    cripto = CriptografiaInventario(chave)

    inventario = cripto.carregar_do_arquivo('inventario.csv')

    while True:
        limpa_tela()
        letreiro()
        x = int(input('''O que você gostaria de fazer?
(0) Sair
(1) Logar
(2) Registrar
-->  '''))

        if x == 0:
            print("Saindo...")
            break
        elif x == 1:
            limpa_tela()
            if login():
                gerenciar_inventario(inventario, cripto)
            break
        elif x == 2:
            limpa_tela()
            cria_usuario()
            break
        elif x == 3:
            limpa_tela()
            cria_usuario()
            break
        else:
            print("Entrada invalida! Digite novamente: ")
            x = int(input())

    cripto.salvar_em_arquivo(inventario, 'inventario.csv')

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

if __name__ == "__main__":
    main()