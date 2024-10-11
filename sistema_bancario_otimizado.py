class Transacao:
    """Classe para representar uma transação bancária."""
    
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return f'{self.tipo}: R$ {self.valor:.2f}'


class Conta:
    """Classe para representar uma conta bancária."""
    
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self._extrato = []  

    def _registrar_transacao(self, tipo, valor):
        """Registra uma transação no extrato."""
        self._extrato.append(Transacao(tipo, valor))

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            self._registrar_transacao("Depósito", valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        """Realiza um saque da conta."""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self._registrar_transacao("Saque", valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Saque não realizado. Verifique o valor e seu saldo.')

    def extrato(self):
        """Exibe o extrato da conta."""
        print(f'\nExtrato da conta de {self.titular}:')
        for transacao in self._extrato:  
            print(transacao)
        print(f'Saldo atual: R$ {self.saldo:.2f}')


def realizar_deposito(conta):
    """Função para gerenciar depósitos."""
    valor = float(input('Digite o valor do depósito: '))
    conta.depositar(valor)


def realizar_saque(conta):
    """Função para gerenciar saques."""
    valor = float(input('Digite o valor do saque: '))
    conta.sacar(valor)


def mostrar_extrato(conta):
    """Função para mostrar o extrato da conta."""
    conta.extrato()


def main():
    """Função principal do sistema bancário."""    
    print("=== Bem-vindo ao Sistema Bancário ===")
    titular = input('Digite o nome do titular da conta: ')
    conta = Conta(titular)

    while True:
        print('\n=== Menu ===')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Extrato')
        print('4. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            realizar_deposito(conta)
        elif opcao == '2':
            realizar_saque(conta)
        elif opcao == '3':
            mostrar_extrato(conta)
        elif opcao == '4':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')

    print("\nDesenvolvido por Matheus Taranto\n")


if __name__ == '__main__':
    main()
