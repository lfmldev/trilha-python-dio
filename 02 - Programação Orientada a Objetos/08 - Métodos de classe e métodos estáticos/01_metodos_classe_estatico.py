class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método ligado a classe e não ao obj da classe como o self, utiliza-se o cls por convensão
    # O método da classe pode acessar e modificar o estado de uma classe, 
    # Já o método estático não pode, pois ele não tem a referência

    @classmethod # Usamos para criar métodos de fábrica que retornam instâncias da classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade) # O cls é a referência para a classe pessoa

    @staticmethod # Método também apontado para a classe, mas sem argumento explícito
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
