from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco): # Método construtor da conta
        self.endereco = endereco # recebe o endereço do cliente
        self.contas = [] # Lista para armazenar as contas do cliente

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta) # Método para registrar conta, que chama o método registrar da transação(class Transacao)

    def adicionar_conta(self, conta):
        self.contas.append(conta) # Ao receber a conta ele adiciona ao array de contas 


class PessoaFisica(Cliente): # Extensão da classe Cliente
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) # herança da classe Cliente(endereco)
        self.nome = nome # Atributos da nova classe
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico() # Vindo da classe Histórico

    @classmethod
    def nova_conta(cls, cliente, numero): # Método de classe que é obrigatório e aponta para a classe Conta
        return cls(numero, cliente) # retorna uma instância de conta

    @property
    def saldo(self):
        return self._saldo   # Métodos para acessar as propiedades da conta, atributos privados.

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor): # Desenho das operações, sacar.
        saldo = self.saldo # Recuperar o saldo 
        excedeu_saldo = valor > saldo # Validação do saldo para saque

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor # débito do saldo
            print("\n=== Saque realizado com sucesso! ===")
            return True # Para dizer que a operação deu certo, serve para a validação

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False # Para dizer que a operação deu errado, serve para a validação

    def depositar(self, valor): # Desenho das operações, depositar.
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3): # Limite e limite_saque tem valores padrões
        super().__init__(numero, cliente)# Recebe os atributos da classe pai
        self.limite = limite # Adiciona mais atributos
        self.limite_saques = limite_saques

    def sacar(self, valor): # Sobrescrita do método sacar da classe pai pois precisa de mais validações
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__] # Aqui esta pegando o nome da classe saque
        ) # Visita a classe Histórico para checar se houve mais de 3 operações do tipo sacar
        # Leia: Para cada transação em histórico de transações se a transação for do tipo saque então guarda na lista e verifica o tamanho da lista

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor) # Se passar nas validações irá buscar o método na classe pai para efetuar o saque

        return False

    def __str__(self): # Método __str__ é a representação da minha classe
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self): # método construtor de histórico
        self._transacoes = [] # lista para agrupar as operações

    @property
    def transacoes(self):
        return self._transacoes # Propriedade para pegar as transações

    def adicionar_transacao(self, transacao): # Aque se recebe a transação do método Transacao e agrupa em um dicionário
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__, # recebe o nome da transação, saque ou depósito
                "valor": transacao.valor, # Valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"), # A hora da transação
            }
        )


class Transacao(ABC): # Classe abstrata, é preciso da biblioteca ABC
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao): # Como ele é uma extensão de Transacao ele precisa respeitar a property e o método abstrato
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor) # Chama o método sacar da conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
