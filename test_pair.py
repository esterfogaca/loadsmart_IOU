from pair import Transacao, Banco

banco = Banco()
t1 = Transacao("george", "ester", 10)
t2 = Transacao("ester", "george", 5)
banco.registrar_transacao(t1)
banco.registrar_transacao(t2)

def test_transaction_1():
  assert([t1.emprestador, t1.emprestado, t1.quantia] == ['george', 'ester', 10])

def test_transaction_2():
  assert([t2.emprestador, t2.emprestado, t2.quantia] == ['ester', 'george', 5])

def test_register_1():
  assert(len(banco.transacoes) == 2)

def test_register_2():
  assert(banco.pega_saldo("george") == 5)
