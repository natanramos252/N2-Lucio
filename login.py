import hashlib

def login():
    usuario = input('Usuario: ')
    senha = input('Senha: ')

    if not usuario_existe(usuario):
        print('Usuario não encontrado!')
    

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

        

def usuario_existe(usuario):
    ##try:
        with open('login.txt','r') as f:
            linhas = f.readlines()

        for i in range (0, len(linhas), 2):
            if linhas [i].strip() == usuario:
                return True
        return False

def remover_usuario(usuario_alvo):
    #lê todas as linhas do usuario
    with open('login.txt','r') as f:
        linhas = f.readlines()

    #lista temporaria pra alocar os usuarios
    usuarios = []
    i = 0
    while i < len(linhas):
        usuario = linhas[i].strip()
        if usuario == usuario_alvo:
            i += 2
        else:
            usuarios.append(linhas[i])
            if i + 1 <len(linhas):
                usuarios.append(linhas[i+1])
            i += 2

        #reescreve o login.txt
    with open('login.txt','w') as f:
        f.writelines(usuarios)

    print(f'Usuario {usuario_alvo} removido com sucesso!')
    
        
            
        
    
    
    
    
        
#criar_usuario()
