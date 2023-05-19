# O que sãi interfaces?
# Define o que uma classe deve fazer e não como ela deve fazer
# Interface seria um padrão definido para se fazer algo
# Interface é como definir um contrato, onde são declarados os métodos e suas assinaturas
# Em python utilizamos classes abstratas para criar estes contratos
# Classes abstratas não podem ser instanciadas

# Similar a herança, mas na classe abstrata a classe filha é obrigada a utilizar os métodos abstratos
# Todos eles

from abc import ABC, abstractmethod, abstractproperty
# É preciso deste módulo ABC para definir as bases das classes abstratas
# E deve-se usar o decorador @abstractmethod

class ControleRemoto(ABC):
    @abstractmethod # método abstrato não terá um corpo e todas as classes filhas serão obrigadas a implementa-la
    def ligar(self):
        pass

    @abstractmethod # Toda vez que se utiliza o método abst, a classe também fica abstr e não pode ser instanciada diretamente
    def desligar(self):
        pass

    @property # Posso forçar também a utilização de uma propriedade em uma classe abstrata
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):

    def ligar(self): # Obrigatóriamente eu preciso chamar este método da classe pai
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self): # Obrigatóriamente eu preciso chamar este método da classe pai
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self): # Obrigatóriamente eu preciso chamar este método da classe pai
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self): # Obrigatóriamente eu preciso chamar este método da classe pai
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
