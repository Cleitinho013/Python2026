import datetime

class Cliente:
    def __init__(self,nome:str, data_nascimento,cpf:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Prato:
    def __init__(self,nome:str, ingredientes: list[str], modo_preparo :str, preco:float):
        self.nome = nome