def enc_maiorchave(d_inventario):
    #função para encontrar maior chave do dicionario
    global chave
    
    if d_inventario == {}:
        chave = 0
    else:
        chave = max(d_inventario.keys())+1

def le_inventario():
    try:
        d_inventario ={}
        with open('inventario.csv','r') as inventario:
            for linha in inventario:
                chave, nome, qt, preco, impor = linha.rstrip().split(';')
                chave = int(chave)
                qt = int(qt)
                preco = float(preco)
                if impor == 'sim' or impor == 's':
                    impor = True
                else:
                    impor = False

                
                d_inventario[chave] = [nome, qt, preco, impor]
        
    except FileNotFoundError:
        print('''Arquivo inventario.cvs não encontrado!
adicione o arquivo ou um novo sera criado''')
           
    return d_inventario
                
def ad_inventario(d_inventario):
    #adiciona itens no inventario
    
    enc_maiorchave(d_inventario)
    
    id = chave + 1
    nome = input('nome do produto: ')
    qt = int(input('quantidade: '))
    preco = float(input('valor: '))
    impor = input('O produto é importado:(sim/ não')

    if impor == 'sim' or impor =='s':
        impor = True
    else:
        impor = False
        
    d_inventario['id'] = [nome, qt, preco, impor]
    
d_inventario = le_inventario()

