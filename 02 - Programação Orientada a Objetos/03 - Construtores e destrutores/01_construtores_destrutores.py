# O construtor é sempre executado quando uma nova instância da classe é formada
# Também camado de inicializador
# O método destrutor é executado para destruir uma instância da classe e liberando memória
# Em python não é muito necessário pois o python tem um coletor de lixo que libera memória
# o método utilizado é o __del__


class Cachorro:
    def __init__(self, nome, cor, acordado=True):  
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):   # O destrutor sempre roda ao final do uso do objeto mesmo declarado antes
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c        # Para ele rodar no momento que for necessário é preciso usar a palavra reservada del

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()