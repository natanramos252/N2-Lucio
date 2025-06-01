import hashlib

def login():
    usuario = input('Usuario: ')
    senha = input('Senha: ')

    h_senha = hashlib.sha256(senha.encode()).hexdigest()
    

def cria_usuario():
    #cria usuario 
    
    usuario = input('Usuario: ')
    senha = input('Senha?: ')
    conf_senha = input('Confirme a senha: ')

    if senha != conf_senha:
        print('as senhas não corresponde')
        senha = input('Senha?: ')
        conf_senha = input('Confirme a senha: ')

    if len(senha) < 8:
        print('so é premitido senhas com mais de 8 cracteres')
        senha = input('Senha?: ')
        conf_senha = input('Confirme a senha: ')
    else:
        h = hashlib.sha256(senha.encode()).hexdigest()
    
    with open('login.txt','a') as f:
        f.write(f'{usuario}|{h}\n')

    print('Usuario criado com sucesso!!')


def autera_usuario(usuario_alvo,n_usuario,h_senha):
    
    #autera usuario
    with open('login.txt','r') as f:
        L = f.readlines()

    with open('login.txt','w') as f:
        for linha in L:
            if usuario_alvo in linha:
                f.write(f'{n_usuario}|{h_senha}\n')
            else:
                f.write(linha)
                
            

