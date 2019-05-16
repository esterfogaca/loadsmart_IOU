class Transacao:

    def __init__(self, emprestador, emprestado, quantia):
        self.emprestador = emprestador
        self.emprestado = emprestado
        self.quantia = quantia

class Banco:
    def __init__(self):
        self.transacoes = list()

    def pega_saldo(self, pessoa):
        emprestou = 0
        pegou_emprestado = 0
        for transacao in self.transacoes:
            if transacao.emprestador == pessoa:
                emprestou = emprestou + transacao.quantia
            if transacao.emprestado == pessoa:
                pegou_emprestado = pegou_emprestado + transacao.quantia

        return emprestou - pegou_emprestado

    def registrar_transacao(self, transacao):
        self.transacoes.append(transacao)

'''
if __name__ == '__main__':
    banco = Banco()
    t1 = Transacao("george", "fulano", 10)
    t2 = Transacao("fulano", "george", 5)
    print(t1.emprestador, t1.emprestado, t1.quantia)
    banco.registrar_transacao(t1)
    banco.registrar_transacao(t2)
    for t in banco.transacoes:
        print(t)
    saldo = banco.pega_saldo("george")
    print(saldo)
'''