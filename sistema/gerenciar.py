from .login import usuario_existe, cria_usuario
from .utils import cabecalho

def listar_usuarios():
    cabecalho("Usuários Cadastrados")
    try:
        with open('login.txt', 'r') as f:
            for l in f:
                nome, _ = l.strip().split('|')
                print(f"- {nome}")
    except FileNotFoundError:
        print("Nenhum usuário encontrado.")

def apagar_usuario():
    cabecalho("Apagar Usuário")
    usuario = input("Usuário a apagar: ").strip()
    if not usuario_existe(usuario):
        print("Usuário não encontrado.")
        return
    with open('login.txt', 'r') as f:
        linhas = f.readlines()
    with open('login.txt', 'w') as f:
        for l in linhas:
            nome, _ = l.strip().split('|')
            if nome != usuario:
                f.write(l)
    print("Usuário apagado.")


def altera_usuario():
    cabecalho("Alterar Usuário")
    antigo = input("Usuário atual: ").strip()
    if not usuario_existe(antigo):
        print("Usuário não existe.")
        return
    novo = input("Novo nome: ").strip()
    if not novo or usuario_existe(novo):
        print("Nome inválido ou já existe.")
        return
    with open('login.txt', 'r') as f:
        linhas = f.readlines()
    with open('login.txt', 'w') as f:
        for l in linhas:
            nome, hs = l.strip().split('|')
            if nome == antigo:
                f.write(f"{novo}|{hs}\n")
            else:
                f.write(l)
    print("Usuário alterado.")

def gerenciar_usuarios():
    while True:
        listar_usuarios()
        print("(0) Sair")
        print("(1) Apagar")
        print("(2) Criar")
        print("(3) Alterar")
        op = input("Escolha: ")
        if op == '0':
            break
        elif op == '1':
            apagar_usuario()
        elif op == '2':
            cria_usuario()
        elif op == '3':
            altera_usuario()
        else:
            print("Opção inválida.")