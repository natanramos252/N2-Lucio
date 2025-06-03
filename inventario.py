def enc_iddisp(d_inventario):
    #função para encontrar maior chave do dicionario
    
    if d_inventario == {}:
        chave = 0
    else:
        chave = max(d_inventario.keys())+1
    return chave

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
                
def ad_inventario(d_inventario, chave):
    #adiciona itens no dicionario inventario
    
    
    #id = chave
    nome = input('nome do produto: ')
    qt = int(input('quantidade: '))
    preco = float(input('valor: '))
    impor = input('O produto é importado:(sim/ não): ')

    if impor == 'sim' or impor =='s':
        impor = True
    else:
        impor = False
        
    d_inventario[chave] = [nome, qt, preco, impor]

    
    return chave+1




d_inventario = le_inventario()
chave = enc_iddisp(d_inventario)
chave = ad_inventario(d_inventario, chave)

