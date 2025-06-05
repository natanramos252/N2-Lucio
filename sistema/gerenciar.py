import hashlib
from sistema.login import *

def gerenciar():
    listar_usuarios()
    r = int(input('''
O que você deseja fazer?          

(1)Apagar algum
(2)Adicionar algum
(3)Modificar algum
--> '''))
    
    if r == 1:
        input_usuario = input('Digite o nome do usuário que deseja apagar: ')
        apagar_usuario(input_usuario)
    elif r == 2:
        cria_usuario()
    elif r == 3:
        input_usuario = input('Digite o nome do usuário que deseja modificar: ')
        usuario_alvo = input('Digite o novo nome de usuário: ')
        altera_usuario(input_usuario, usuario_alvo)

def listar_usuarios():
    print('\n--- Usuários registrados ---')
    try:
        with open('login.txt', 'r') as f:
            for linha in f:
                nome, _ = linha.strip().split('|')
                print(f'- {nome}')
    except FileNotFoundError:
        print('Nenhum usuario encontrado!')