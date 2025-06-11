from sistema import *

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_inventario():

    cabecalho(texto='controle de inventario\n')
    print('O que você gostaria de fazer?')
    print('(1) cadastrar produtos ')
    print('(2) apagar produto')
    print('(3) consultar')
    print('(4) mostra todo o inventario')
    
    x = int(input('opção: '))
    

    while True:
        if x == 1:
            ad_inventario(d_inventario, chave)
            break
        elif x == 2:
            apaga_iten()
            break
        elif x == 3:
            #LimpaTela()
            busca_nome(d_inventario)
            break
        elif x == 4:
            imp_inventario(d_inventario)
            break
            
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
    #LimpaTela()
    cabecalho(texto = 'adciona itens')

    while True:
    
        nome = input('nome do produto: ')

        if not nome:
            print('Cadastro de produtos finalizados')
            menu_inventario()
            break

        try:      
            qt = int(input('quantidade: '))
            preco = float(input('valor: '))
            impor = input('O produto é importado:(sim/ não): ')

            if impor == 'sim' or impor =='s':
                impor = True
            else:
                impor = False
                
            d_inventario[chave] = [nome, qt, preco, impor]
            chave +=1
        except ValueError: 
            print("Erro: Digite valores numéricos válidos para quantidade e preço!")
            continue  

            
    return chave
    

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
        empurra(L, n, posicao)
        n -= 1

def ordena(dicionario, algoritmo='bubble'):
    L = list(dicionario.items())
    if algoritmo == 'bubble':
        
        bubble_sort(L)
    else:
        0#merge

    return L
    
        
def busca_nome(dicionario):
    produto = input('qual produto: ')

    quant = len(dicionario)

    if quant <= 50:
              
        for chave, dados in L():
            nome = dados[0]
            qt = dados[1]
            preco = dados[2]
            impor = dados[3]
            if produto == nome:
                print(f'{chave}: {nome}| {qt}| {preco}| {impor}')
                break
        else:
            print('item não existe')
    else:
        if quant <=100:
            ordena(dicionario, 'bubble')
        else:
            ordena(dicionario, 'merge')
    #faz a busca binaria
                            
d_inventario = le_inventario()
chave = enc_iddisp(d_inventario)
#chave = ad_inventario(d_inventario, chave)

#print(d_inventario)
#imp_inventario(d_inventario) 
