# Encapsulamento é a ideia de agrupar os dados e métodos que não devem ser acessíveis diretamente
# A proteção das variáveis e mtétodos, estas só devem ser acessadas por outros métodos da classe.
# Todo recurso é público em python. 
# Por convensão é utilizada um underline antes do nome do atributo/variável que não deve ser acessada.
# Isto esta relacionado ao acesso público e privado
# Público = pode ser acessado de fora da classe
# Privado = só pode ser acessado pela classe

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # variável privada!!
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ... Aqui seria a forma correta de acessar a variável saldo, com o acesso pela classe
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
