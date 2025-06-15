import hashlib
from typing import Dict, List, Union

class CriptografiaInventario:
    def __init__(self, chave: str, salt: str = None):
        if not chave or len(chave) < 4:
            raise ValueError("A chave deve ter pelo menos 4 caracteres.")
        self.chave = chave
        self.salt = salt if salt else "s3gIn@2023"
        self.deslocamento = self._gerar_deslocamento()

    def _gerar_deslocamento(self) -> int:
        hash_obj = hashlib.sha256((self.chave + self.salt).encode('utf-8'))
        hash_hex = hash_obj.hexdigest()
        return sum(ord(c) for c in hash_hex) % 23 + 3

    def _processar_texto(self, texto: str, operacao: str) -> str:
        if not isinstance(texto, str):
            texto = str(texto)
        resultado = []
        desloc = self.deslocamento if operacao == 'criptografar' else -self.deslocamento
        for char in texto:
            codigo = ord(char)
            if 32 <= codigo <= 126:
                novo_codigo = codigo + desloc
                while novo_codigo > 126:
                    novo_codigo -= 95
                while novo_codigo < 32:
                    novo_codigo += 95
                resultado.append(chr(novo_codigo))
            else:
                resultado.append(char)
        return ''.join(resultado)

    def criptografar_dados(self, dados: Dict[int, List[Union[str, int, float, bool]]]) -> Dict[int, List[str]]:
        dados_cripto = {}
        for id_prod, campos in dados.items():
            campos_cripto = [
                self._processar_texto(campos[0], 'criptografar'),
                self._processar_texto(campos[1], 'criptografar'),
                self._processar_texto(campos[2], 'criptografar'),
                self._processar_texto(campos[3], 'criptografar')
            ]
            dados_cripto[id_prod] = campos_cripto
        return dados_cripto

    def descriptografar_dados(self, dados: Dict[int, List[str]]) -> Dict[int, List[Union[str, int, float, bool]]]:
        dados_descripto = {}
        for id_prod, campos in dados.items():
            campos_descripto = [
                self._processar_texto(campos[0], 'descriptografar'),
                int(self._processar_texto(campos[1], 'descriptografar')),
                float(self._processar_texto(campos[2], 'descriptografar')),
                self._processar_texto(campos[3], 'descriptografar') == 'True'
            ]
            dados_descripto[id_prod] = campos_descripto
        return dados_descripto

    def salvar_em_arquivo(self, dados: Dict[int, List[Union[str, int, float, bool]]], nome_arquivo: str):
        dados_criptografados = self.criptografar_dados(dados)
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            for id_prod, campos in dados_criptografados.items():
                linha = f"{id_prod};{';'.join(campos)}\n"
                f.write(linha)

    def carregar_do_arquivo(self, nome_arquivo: str) -> Dict[int, List[Union[str, int, float, bool]]]:
        dados_lidos = {}
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    partes = linha.strip().split(";")
                    id_prod = int(partes[0])
                    dados_lidos[id_prod] = partes[1:]
            return self.descriptografar_dados(dados_lidos)
        except FileNotFoundError:
            return {}
