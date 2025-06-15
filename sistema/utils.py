import os

def limpa_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(texto=''):
    """Imprime um cabeçalho para organização visual."""
    print('-'*80)
    if texto:
        print(texto.upper().center(80))
        print('-'*80)

def bubble_sort(arr, key=None):
    if key is None:
        key = lambda x: x
    L = list(arr)
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key(L[j]) > key(L[j + 1]):
                L[j], L[j + 1] = L[j + 1], L[j]
    return L