class Estudante:
    escola = "DIO" # Atributo de classe, é comum para as instâncias

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1) # Atributo de instância, único para cada instância
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" # A troca do atributo de classe influencia em todos os atributos criados após a troca 

# aluno_1.escola = "Python" # Irá trocar apenas da instância apontada

aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
