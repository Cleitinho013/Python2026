class Pessoa():
    def __init__(self, nome, telefone, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Nascimento: {self.data_nascimento}"

class Mecanico():
    def __init__(self, pessoa):
        self.pessoa =  pessoa

    def __str__(self):
        return f'''Pessoa: {self.pessoa}''' 

class Cliente():
    def __init__(self, pessoa, email):
        self.pessoa = pessoa
        self.email = email

    def __str__(self):
        return f"Pessoa: {self.pessoa}, Email: {self.email}"
        
class Servico():
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"Descricao: {self.descricao}, Valor: {self.valor}" 
        
class Servico_realizado():
    def __init__(self, servico, mecanico):
        self.servico = servico
        self.mecanico = mecanico
        
    def __str__(self):
        return f"Servico: {self.servico}, Mecanico: {self.mecanico}" 

class Ordem_servico():
    def __init__(self, data_entrada, veiculo, data_saida, cliente, desconto, servicos):
        self.data_entrada = data_entrada
        self.veiculo = veiculo
        self.data_saida = data_saida
        self.cliente = cliente
        self.desconto = desconto
        self.servicos = servicos
    
    def CalularTotal(self):
        total = 0
        for i in self.servicos:
            total = total + i.servico.valor
        total=total-self.desconto
        return total
    
    def printarServicos(self):
        a = ""
        for i in self.servicos:
            a = a + f"{i.servico.descricao};"
        return a

    def __str__(self):
        return f"Entrada: {self.data_entrada}, {self.veiculo}, Saida: {self.data_saida}, Cliente: {self.cliente.pessoa.nome}, Desconto: {self.desconto}, serviços realizados: {self.printarServicos()}, Total: {self.CalularTotal()}" 
        
class Veiculo():
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f"Placa: {self.placa}, Cor: {self.cor}"
        
class Moto(Veiculo):
    def __init__(self, placa, cor):
        super().__init__(placa, cor)

    def __str__(self):
        return f"{super().__str__()}"

class VeiculoComPassageiro(Veiculo):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor)
        self.lugares = lugares

    def __str__(self):
        return f"{super().__str__()}, Lugares: {self.lugares}"
        
class Carro(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares, portas):
        super().__init__(placa, cor, lugares)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()}, Portas: {self.portas}"

class Onibus(VeiculoComPassageiro):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return f"{super().__str__()}"




pess1 = Pessoa("João", "(47)123456", "28/01/2010")
pess2 = Pessoa("Mario", "(47)654321", "02/12/2009")
mec1 = Mecanico(pess2)
cli1 = Cliente(pess1, "joao.joao@gmail.com")
car1 = Carro("ythh-4534634", "branco", 5, 4)
mot1 = Moto("gfhfg-2353456435474356", "preto")
ser1 = Servico("troca de pneu", 250)
ser2 = Servico("troca de óleo", 100)
serre2 = Servico_realizado(ser2, mec1)
serre1 = Servico_realizado(ser1, mec1)
lstser = [serre1,serre2]
ord_ser = Ordem_servico("25/04/2026", car1, "26/04/2026", cli1, 20, lstser)

print(ord_ser)
print(mot1)
