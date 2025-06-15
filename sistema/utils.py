import os

def limpa_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(texto=''):
    """Imprime um cabeçalho para organização visual."""
    print('-'*50)
    if texto:
        print(texto.upper())
        print('-'*50)
