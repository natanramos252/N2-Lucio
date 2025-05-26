import hashlib

def login():
    usuario = input('Usuario: ')
    senha = input('Senha: ')

    if not usuario_existe(usuario):
        print('Usuario não encontrado!')
    

def criar_usuario():
    #função para criar usuario converte a senha para um hash usando o algoritimo
    #sha256 para cripitografar a senha e impedir que a mesmo possa ser convertida
    #a original
    usuario = input('Usuario: ')

    if usuario_existe(usuario):
        print ('ERRO: Usuario já exite!!!')
        
    senha = input('Digite a senha: ')
    conf_senha = input('Confirme a senha: ')

    if conf_senha == senha:
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()

        with open ('login.txt', 'r') as f:
            f.write (usuario + '\n')
            f.write (hash_senha)
        f.close()
        print('Usuario criado com sucesso!')

    else:
        print('As senhas não são iguais')

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
