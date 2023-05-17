# Neste exemplo se criou uma propriedade dade para se calcular a idade de uma pessoa
# desta forma não se faz necessário criar uma variável para armazenamento desta variável
# assim somente haverá um chamado desta função se for necessário 

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property 
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
