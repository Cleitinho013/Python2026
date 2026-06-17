class Veiculo:
    def __init__(self, placa:str, ano:int):
        self.placa = placa
        self.ano = ano

class Moto(Veiculo):
    def __init__(self, placa, ano):
        super().__init__(placa, ano)

class Caminhao(Veiculo):
    def __init__(self, placa, ano, peso_em_kg:int):
        super().__init__(placa, ano)
        self.peso_em_kg = peso_em_kg
igor=Moto("765w6uyjng", -99)
vitao=Caminhao("kyitd76içkug",67,6767)
print(igor.placa)
print(igor.ano)
print(vitao.placa)
print(vitao.ano)
print(vitao.peso_em_kg)