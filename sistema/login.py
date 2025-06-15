import hashlib
from getpass import getpass
from .utils import cabecalho


def login():
    cabecalho("Login")
    usuario = input("Usuário: ").strip()
    senha = getpass("Senha: ")
    h = hashlib.sha256(senha.encode()).hexdigest()
    try:
        with open('login.txt', 'r') as f:
            for l in f:
                nome, hs = l.strip().split('|')
                if usuario == nome and h == hs:
                    print("Login bem-sucedido!")
                    return True
    except FileNotFoundError:
        print("Nenhum usuário cadastrado, Criando...")
        cria_usuario()
        return True
    print("Dados incorretos ou usuário não existe, deseja criar um novo? (0) Não e (1) Sim")
    if int(input("--> ")) == 1:
        cria_usuario()
        return True
    else:
        return False

def usuario_existe(usuario):
    try:
        with open('login.txt', 'r') as f:
            for l in f:
                nome, _ = l.strip().split('|')
                if nome == usuario:
                    return True
    except FileNotFoundError:
        return False
    return False

def cria_usuario():
    cabecalho("Criar novo usuario")
    usuario = input('Usuario: ').strip()

    if not usuario:
        print("Nome de usuário não pode ser vazio.")
        return
    if usuario_existe(usuario):
        print("Usuário já existe.")
        return
    while True:
        senha = getpass("Senha: ")
        conf = getpass("Confirme a senha: ")
        if senha != conf:
            print("As senhas não coincidem.")
        elif len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
        else:
            break
    h = hashlib.sha256(senha.encode()).hexdigest()
    with open('login.txt', 'a') as f:
        f.write(f"{usuario}|{h}\n")
    print("Usuário criado com sucesso!")


def altera_usuario(usuario_alvo, novo_usuario):

    with open('login.txt','r') as f:
        linhas = f.readlines()

    with open('login.txt','w') as f:
        for linha in linhas:
            nome, hash = linha.strip().split('|')
            if nome == usuario_alvo:
                f.write(f'{novo_usuario}|{hash}\n')
            else:
                f.write(linha)

def apagar_usuario(input_usuario):

    with open('login.txt','r') as f:
        linhas = f.readlines()

    with open('login.txt','w') as f:
        for linha in linhas:
            if input_usuario not in linha.strip().split(':')[0]:
                f.write(linha)
            

    
