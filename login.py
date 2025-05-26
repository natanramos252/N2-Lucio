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

        with open ('login.txt', 'a') as f:
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
    
    
    
        
login()
