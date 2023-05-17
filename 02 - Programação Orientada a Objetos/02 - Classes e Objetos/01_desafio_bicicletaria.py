# Tudo em python é objeto e classes são como objetos da vida real
# Na classe definimos as características e comportamentos de um objeto
# Mas não conseguimos utiliza-las diretamente
# Já os objeto podemos usar com as caracteristicas e comportamentos de uma classe
# Atributos são as características comuns da classe
# e os métodos são funções que estão dentro de uma classe
# Os médotos são como o comportamento que as classes podem tomar

class Bicicleta:                                   # Palavra reservada para criação de uma classe
    def __init__(self, cor, modelo, ano, valor):   # Init é o construtor o que inicia a classe
        self.cor = cor                             # self representa a instância do objeto
        self.modelo = modelo                       # Assim construimos uma classe com atributos
        self.ano = ano
        self.valor = valor

    def buzinar(self):                             # self é a referência explicita ao objeto
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)      # Instância de uma bicicleta
b1.buzinar()                                        # Chama os métodos
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)          # Posso acessar os atributos da classe

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
