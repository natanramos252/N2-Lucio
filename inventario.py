def enc_iddisp(d_inventario):
    #função para encontrar maior chave do dicionario
    
    if d_inventario == {}:
        chave = 0
    else:
        chave = max(d_inventario.keys())+1
    return chave

def caminho():

    caminho = 'inventario.csv'
    x= int(input('''1 - para indicar um caminho
              2 - para criar um novo arquivo'''))

    while True:
        if x == 1:
            caminho = imput('informe o caminho: ')
            break
        else:
            break
            
    return caminho
    
def le_inventario():
    #adiciona o conteudo do arquivo em um dicionario
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
        print('''Arquivo inventario.csv não encontrado!!!!
adicione o arquivo ou um novo sera criado.''')
        caminho()        

        
           
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

def apaga_iten(d_inventario, chave):
    del d_inventario[chave]

    return d_inventario

def grava_inventario(d_inventario):
    with open('inventario.csv','w') as inventario:
        for chave, dados in d_inventario.items():
            nome = dados[0]
            qt = dados[1]
            preco = dados[2]
            impor = dados[3]
            inventario.write(f'{chave};{nome};{qt};{preco};{impor}\n')

def imp_inventario(dicionario):
    m_nome = 0
    produtos = 'produtos'
    
    #esta dando erro de sintax
    print('-'*80)
    print(f'{'produtos':^80}')
    print('-'*80)

    for chave, dados in dicionario.items():
        if m_nome < len(dados[0]):
            m_nome = len(dados[0])

           

    for chave, dados in dicionario.items():
        nome = dados[0]
        qt = dados[1]
        preco = dados[2]
        impor = dados[3]
        if impor == True:
            impor = 'importado'
        else:
            impor ='nacional'
        print(f'{chave}: {nome:^{m_nome}}| {qt:>6}| {preco:>10.2f}| {impor:^10}')
        #print(f'{nome} | {qt}| {preco}| {impor}')


def busca_nome(dicionario):
    produto = input('qual produto: ')
    for chave, dados in dicionario.items():
        nome = dados[0]
        qt = dados[1]
        preco = dados[2]
        impor = dados[3]
        if produto == nome:
            print(f'{chave}: {nome}| {qt}| {preco}| {impor}')

            #print('print(f'{chave}: {nome}| {qt:>6}| {preco}| {impor}')')

d_inventario = le_inventario()
chave = enc_iddisp(d_inventario)
#chave = ad_inventario(d_inventario, chave)

#print(d_inventario)
#imp_inventario(d_inventario) 
