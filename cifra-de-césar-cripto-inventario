import hashlib
import os
from typing import Dict, List, Union

class criptografiaInventário:
    #Classe responsável por criptografar e descriptografar os dados do inventário usando uma cifra de César modificada com chave derivada de hash SHA-256.


    def __init__(self, chave: str, salt: str = None):
    #Inicializa o sistema de criptografia com uma chave secreta.
    #Args: chave (str): Chave secreta para criptografia (senha do usuário) 
            #salt (str, optional): Valor adicional para aumentar segurança.
        if not chave or len (chave) < 4:
            raise ValueError ("a chave deve ter pelo menos 4 caracteres")
        
        self.chave = chave
        self.salt = salt if salt else "s3gIn@2023" #salt padrao a ser modificado
        self.deslocamento = self.gerar_deslocamento()

    def _gerar_deslocamento(self) -> int:
        #Gera um deslocamento único baseado na chave e salt usando SHA-256
        hash_obj = hashlib.sha256((self.chave + self.salt).encode('utf-8'))
        hash_hex = hash_obj.hexdigest()
        return sum(ord(c) for c in hash_hex) % 23 + 3 #desloc entre 3 - 25
    
    def _processar_texto(self, texto, str, operacao: str) -> str:
        #Processa o texto para criptografar ou descriptografar
        #Args: texto (str): Texto a ser processado
                #operacao (str): 'criptografar' ou 'descriptografar'
        #Returns:
            #str: Texto processado
        if not isinstance(texto, str):
            texto = str(texto)
        resultado = []
        desloc = self.deslocamento if operacao == 'criptografar' else -self.deslocamento

        for char in texto:
            codigo = ord(char)
            #Aplica apenas a caracteres ASCII imprimíveis (32-126)
            if 32 <= codigo <= 126:
                novo_codigo = codigo + desloc
            #Trata overflow/underflow
                while novo_codigo > 126:
                        novo_codigo -= 95
                while novo_codigo < 32:
                        novo_codigo += 95
                resultado.append(chr(novo_codigo))
            else: 
                resultado.append (char)
        return ''.join(resultado) 

    def criptografar_dados(self, dados: Dict[int, List[Union[str, int, float, bool]]]) -> Dict(int, List[str]]):
        #Criptografa todos os campos de um dicionário de inventário
        #Args:
            #dados (Dict): Dicionário com os dados originais {id: [nome, qtd, preço, importado]}                   
            #Returns:
            #Dict: Dicionário com todos os campos criptografados
        if not isinstance(dados, dict):
            raise TypeError("Dados devem ser dicionário") 
            
        dados_cripto = {}

        for id_prod, campos in dados.items():
            try:
                 campos_cripto = [
                    self._processar_texto(campos[0], 'criptografar'), #nome
                    self.processar
