# Herança multipla uma classe herda de duas classes características distintas

class Animal: # Classe pai
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self): # Formatação para exibir atributos da classe
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal): # Classe filha
    def __init__(self, cor_pelo, **kw): # Para buscar os atributos da classe pai sem entrar em conflito de quantidade
        self.cor_pelo = cor_pelo        # de atributos é necessário utilizar kwargs, deve haver sempre chave e valor
        super().__init__(**kw)          # e apontar com a palavra reservada super()


class Ave(Animal): # Classe filha 
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero): # Classe neta
    pass


class Ornitorrinco(Mamifero, Ave): # herança multipla, neta de animal e filha de mamífero e ave
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__) # método para verificar a orden de execução das classes
        # print(Ornitorrinco.mro())
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto") # Ao utilizar kw deve se passar chave e valor
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja") 
print(ornitorrinco)  
