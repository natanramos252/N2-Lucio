from .utils import cabecalho


def salva_inventario(inv):
    with open('inventario.csv', 'w') as f:
        for idp, d in inv.items():
            f.write(f"{idp};{d[0]};{d[1]};{d[2]};{d[3]}\n")

def prox_id(inv):
    return max(inv.keys(), default=0) + 1

def buscar_produto(inv):
    cabecalho("Buscar Produto")
    termo = input("Nome: ").strip().lower()
    itens = sorted(inv.items(), key=lambda x: x[1][0].lower())
    nomes = [i[1][0].lower() for i in itens]
    if len(nomes) > 50:
        # Busca binária
        l, r = 0, len(nomes)-1
        while l <= r:
            m = (l+r)//2
            if nomes[m] == termo:
                idp = itens[m][0]
                break
            elif termo < nomes[m]:
                r = m-1
            else:
                l = m+1
        else:
            print("Não encontrado.")
            return
    else:
        # Busca linear
        for nome_lower, (idp, _) in zip(nomes, itens):
            if termo == nome_lower:
                break
        else:
            print("Não encontrado.")
            return
    d = inv[idp]
    print(f"Encontrado ID {idp}: {d[0]} | {d[1]} | {d[2]} | {d[3]}")
            
def adicionar_produto(inv):
    cabecalho("Adicionar Produto")
    while True:
        nome = input("Nome (vazio para sair): ").strip()
        if not nome:
            break
        try:
            qt = int(input("Quantidade: "))
            preco = float(input("Preço: "))
        except ValueError:
            print("Quantidade/Preço inválido.")
            continue
        imp = input("Importado? (s/n): ").strip().lower() in ['s','sim']
        idp = prox_id(inv)
        inv[idp] = [nome, qt, preco, imp]
        print(f"Cadastrado ID {idp}.")
    salva_inventario(inv)

def apagar_produto(inv):
    cabecalho("Apagar Produto")
    try:
        idp = int(input("ID: "))
    except ValueError:
        print("ID inválido.")
        return
    if idp in inv:
        del inv[idp]
        salva_inventario(inv)
        print("Apagado com sucesso.")
    else:
        print("ID não encontrado.")

def buscar_produto(inv):
    cabecalho("Buscar Produto")
    termo = input("Nome: ").strip().lower()
    itens = sorted(inv.items(), key=lambda x: x[1][0].lower())
    nomes = [i[1][0].lower() for i in itens]
    if len(nomes) > 50:
        # Busca binária
        l, r = 0, len(nomes)-1
        while l <= r:
            m = (l+r)//2
            if nomes[m] == termo:
                idp = itens[m][0]
                break
            elif termo < nomes[m]:
                r = m-1
            else:
                l = m+1
        else:
            print("Não encontrado.")
            return
    else:
        # Busca linear
        for nome_lower, (idp, _) in zip(nomes, itens):
            if termo == nome_lower:
                break
        else:
            print("Não encontrado.")
            return
    d = inv[idp]
    print(f"Encontrado ID {idp}: {d[0]} | {d[1]} | {d[2]} | {d[3]}")

def grava_inventario(d_inventario):
    with open('inventario.csv','w') as inventario:
        for chave, dados in d_inventario.items():
            nome = dados[0]
            qt = dados[1]
            preco = dados[2]
            impor = dados[3]
            inventario.write(f'{chave};{nome};{qt};{preco};{impor}\n')


def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def empurra(L, n,posicao):
    i = 0
    while i < n - 1:
        if L[i][posicao] < L[i + 1][1][posicao]:
            troca(L, i, i + 1)
        i += 1
        
def bubble_sort(L, posicao=0):
    n = len(L)
    while n>1:
        empurra(L, n, posicao)
        n -= 1
        
def ordena(dicionario, algoritmo='bubble'):
    L = list(dicionario.items())
    if algoritmo == 'bubble':
        
        bubble_sort(L)


def mostrar_inventario(inv):
    L = inv
    impor = ' '
    
    cabecalho("Inventário")
    if not inv:
        print("Vazio.")
        return
                                  
    for idp, d in sorted(list(inv.items())):
        if d[3] == True:
            impor = 'importado'
        else:
            impor = 'nacional'
        
       
        print(f"ID{idp}: {d[0]:^20} | {d[1]:>6} | {d[2]:10.2f} | {impor}")


