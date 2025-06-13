def menu_inventario():

    print('(1) cadastrar produto')
    print('(2) apagar produto')
    print('(3) consultar produto')
    print('(4) impromi na tela todos os procutos')
    x = input('qual opção: ')

    while True:
        if x == 1:
            ad_inventario()
            break
        elif x == 2:
            y = int(input('''Digite o id do produto que deseja apagar: '''))
            if y not in d_inventario:
                print('id não encontrado!')
            else:
                apaga_item()
            break
        elif x == 3:
            
            break
        elif x==4:
            imp_inventario(d_inventario)
        else:
            print("Entrada invalida! Digite novamente: ")
            x = int(input())


def enc_iddisp(d_inventario):
    #função para encontrar maior chave do dicionario
    
    if d_inventario == {}:
        chave = 0
    else:
        chave = max(d_inventario.keys())+1
    return chave

def caminho():
    
    caminho = input('informe o caminho: ')
    return caminho
    
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
        print('''Arquivo inventario.csv não encontrado!!!! adicione o arquivo ou um novo sera criado.
              
              1 - para indicar um caminho
              2 - para criar um novo arquivo''')
        opção = int(input())

        
           
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

def apaga_item(d_inventario, chave):
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
    #esta dando erro de sintax
    print('---'*20)
    print('produtos')
    print('---'*20)

    for chave, dados in dicionario.items():
        nome = dados[0]
        qt = dados[1]
        preco = dados[2]
        impor = dados[3]
        print(f'{chave}: {nome} | {qt}| {preco}| {impor}')
        #print(f'{nome} | {qt}| {preco}| {impor}')




d_inventario = le_inventario()
chave = enc_iddisp(d_inventario)
#chave = ad_inventario(d_inventario, chave)

#print(d_inventario)
imp_inventario(d_inventario) 
def enc_iddisp(d_inventario):
    #função para encontrar maior chave do dicionario
    
    if d_inventario == {}:
        chave = 0
    else:
        chave = max(d_inventario.keys())+1
    return chave

def def_caminho(caminho):

    #caminho = 'inventario.csv'
    print('1 - para indicar um caminho')
    print('2 - para criar um novo arquivo')
    x= int(input('opção: '))
    
    if x == 1:
        
        return input('informe o caminho: ')
    
    else:
        arq = open('inventario.csv','w')
        arq.close()
        
        return 'inventario.csv'
    
def le_inventario():
    caminho = 'inventario.csv'
    while True:
        
        try:
            arq = open(caminho,'r')
            
        except FileNotFoundError:
            caminho = def_caminho(caminho)
        else:
            arq.close()
            break
        
            
    
    #adiciona o conteudo do arquivo em um dicionario
    try:
        
        with open(caminho,'r') as inventario:
            d_inventario ={}
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
        
    except :
        print('''erro.''')
        #def_caminho(caminho)        

        
           
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

def cabecalho(texto):
    
    print('-'*80)
    print(f'{texto:^80}')
    print('-'*80)

def imp_inventario(dicionario):
    m_nome = 0
    produtos = 'produtos'

    cabecalho(texto='produtos')
  
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
        empura(L, n, posicao)
        n -= 1

def ordena(L):
    L = list(dicionaio.items())
    bubble_sort(L)

    return L
    
        
def busca_nome(dicionario):
    produto = input('qual produto: ')
    
    #ordena(dicionario)
    #L = list(dicionario.items())# converte
    
    #qlinha = 0 
    #for x in L:
    #    qlinha += 1
        
    for chave, dados in dicionario.items():
        nome = dados[0]
        qt = dados[1]
        preco = dados[2]
        impor = dados[3]
        if produto == nome:
            print(f'{chave}: {nome}| {qt}| {preco}| {impor}')
    else:
        print('item não existe')
            
d_inventario = le_inventario()
chave = enc_iddisp(d_inventario)
#chave = ad_inventario(d_inventario, chave)

#print(d_inventario)
#imp_inventario(d_inventario) 
