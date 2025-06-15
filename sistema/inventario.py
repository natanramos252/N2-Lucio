from .utils import cabecalho, bubble_sort

def salva_inventario(inv):
    """Grava o inventário em disco (não criptografado)."""
    with open('inventario.csv', 'w', encoding='utf-8') as f:
        for idp, d in inv.items():
            f.write(f"{idp};{d[0]};{d[1]};{d[2]};{d[3]}\n")

def prox_id(inv):
    return max(inv.keys(), default=0) + 1

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
        imp = input("Importado? (s/n): ").strip().lower() in ['s', 'sim']
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
    itens = bubble_sort(
        list(inv.items()),
        key=lambda x: x[1][0].lower()
    )
    nomes = [item[1][0].lower() for item in itens]

    if len(nomes) > 50:
        # Busca binária
        l, r = 0, len(nomes) - 1
        while l <= r:
            m = (l + r) // 2
            if nomes[m] == termo:
                idp = itens[m][0]
                break
            elif termo < nomes[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            print("Não encontrado.")
            return
    else:
        # Busca linear
        for name, (idp, _) in zip(nomes, itens):
            if name == termo:
                break
        else:
            print("Não encontrado.")
            return

    d = inv[idp]
    print(f"Encontrado ID {idp}: {d[0]} | Qtde: {d[1]} | Preço: {d[2]} | Importado: {d[3]}")

def mostrar_inventario(inv):
    cabecalho("Inventário")
    if not inv:
        print("Inventário vazio.")
        return
    itens = bubble_sort(
        list(inv.items()),
        key=lambda x: x[0]
    )

    for idp, d in itens:
        tipo = 'importado' if d[3] else 'nacional'
        print(f"ID {idp}: {d[0]:<20} | {d[1]:>6} | {d[2]:10.2f} | {tipo}")

def gerenciar_inventario(inv, cripto):
    """Menu do inventário, salvando criptografado após cada ação."""
    while True:
        cabecalho("Menu Inventário")
        print("(0) Voltar")
        print("(1) Cadastrar produto")
        print("(2) Apagar produto")
        print("(3) Buscar produto")
        print("(4) Mostrar inventário")
        escolha = input("Escolha: ").strip()

        if escolha == '0':
            break
        elif escolha == '1':
            adicionar_produto(inv)
        elif escolha == '2':
            apagar_produto(inv)
        elif escolha == '3':
            buscar_produto(inv)
        elif escolha == '4':
            mostrar_inventario(inv)
        else:
            print("Opção inválida!")

        # Salva sempre criptografado
        cripto.salvar_em_arquivo(inv, 'inventario.csv')
