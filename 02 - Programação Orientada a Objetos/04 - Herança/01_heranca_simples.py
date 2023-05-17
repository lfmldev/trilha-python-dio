# Herança é justamente herdar da classe pai as características e comportamentos
# é possível também herdar uma classe em níveis mais distantes como uma classe neta


class Veiculo:   # Classe pai
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    # Formatação para apresentar os atributos da classe pode ser reutilizado para facilitar a leitura da classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo): # Classe filha, tem os mesmo atributos
    pass


class Carro(Veiculo): # Classe filha, tem os mesmo atributos
    pass


# Se for usar outro contrutor e quiser utilizar os atributos da classe pai,
# é preciso apontar a classe pai ou então irá sobrescrever os atributos
# Para apontar para a classe pai é preciso utilizar a palavra reservada super().__init__
# Se não for utilizado o método fica limitado ao escopo

class Caminhao(Veiculo): # Classe filha com novos atributos e métodos exclusivos desta classe
    def __init__(self, cor, placa, numero_rodas, carregado):    
        super().__init__(cor, placa, numero_rodas)               
        self.carregado = carregado                              

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
