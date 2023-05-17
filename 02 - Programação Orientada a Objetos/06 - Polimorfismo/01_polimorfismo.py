# Polimorfismo: dependendo do objeto, ele vai variar a sua forma de agir
# Exemplo a função len()
# len("python") e len([10,20,30]) entradas diferentes e formas diferentes de agir
# Polimorfismo com herança a classe filha herda mais modifica os método para encaixar melhor em sua
# funcionalidade

class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj): # Aqui está o polimorfismo pois buscou o método de interesse na classe
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
