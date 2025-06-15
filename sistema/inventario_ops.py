from .utils import (cabecalho, limpa_tela)
from .cifra_cripto_inventario import CriptografiaInventario
from .inventario import (
    adicionar_produto,
    apagar_produto,
    buscar_produto,
    mostrar_inventario
)

def le_inventario():
    """Descriptografa e carrega inventário em memória."""
    cripto = CriptografiaInventario(input("Chave p/ descriptografar: ").strip())
    return cripto.carregar_do_arquivo('inventario.csv')

def gerenciar_inventario(inv, cripto):
    """Menu de gerenciamento que já salva em disco cifrado após cada ação."""
    while True:
        cabecalho("Menu Inventário")
        print("(0) Voltar")
        print("(1) Cadastrar")
        print("(2) Apagar")
        print("(3) Buscar")
        print("(4) Mostrar tudo")
        escolha = input("Escolha: ").strip()

        if escolha == '0':
            #main()
            break
        elif escolha == '1':
            limpa_tela()
            adicionar_produto(inv)
        elif escolha == '2':
            limpa_tela()
            apagar_produto(inv)
        elif escolha == '3':
            limpa_tela()
            buscar_produto(inv)
        elif escolha == '4':
            limpa_tela()            
            mostrar_inventario(inv)
        else:
            print("Opção inválida.")

        cripto.salvar_em_arquivo(inv, 'inventario.csv')
