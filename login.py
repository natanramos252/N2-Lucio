import hashlib



def login():
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    h_senha = hashlib.sha256(senha.encode()).hexdigest()
    autenticado = False

    try:
        with open('login.txt','r') as f:
            for linha in f:
                nome, hash_senha = linha.strip().split('|')
                if usuario  == nome and h_senha == hash_senha:
                    autenticado = True
                    break

        if autenticado:
            print('Login bem sucedido!')    
        else:
            if not (usuario_existe(usuario)):
                print("Usuario, nao existente, criando...")
                cria_usuario()
            else:
                print('Dados incorretos!')
            
    except FileNotFoundError:
        print(f'{h_senha}')
        print('Nenhum usuario cadastrado \n Cria um usuario e senha')
        cria_usuario()

def usuario_existe(usuario):
    try:
        with open('login.txt', 'r') as f:
            for linha in f:
                nome, _ = linha.strip().split('|')
                if usuario == nome:
                    return True
    except FileNotFoundError:
         return False
    return False

def cria_usuario():
    #cria usuario 
    
    usuario = input('Usuario: ')

    while True:
        senha = input('Senha: ')
        conf_senha = input('Confirme a senha: ')

        if senha != conf_senha:
            print('as senhas não coincidem.')

        elif len(senha) < 8:
            print('A senha deve ter pelo menos 8 caracteres.')
        else:
            h = hashlib.sha256(senha.encode()).hexdigest()
            break
        
    with open('login.txt','a') as f:
        f.write(f'{usuario}|{h}\n')

    print('Usuario criado com sucesso!!')


def altera_usuario(usuario_alvo, novo_usuario, nova_senha):
    h_senha = hashlib.sha256(nova_senha.encode()).hexdigest()

    with open('login.txt','r') as f:
        linhas = f.readlines()

    with open('login.txt','w') as f:
        for linha in linhas:
            nome, _ = linha.strip().split('|')
            if nome == usuario_alvo:
                f.write(f'{novo_usuario}|{h_senha}\n')
            else:
                f.write(linha)
                
            

