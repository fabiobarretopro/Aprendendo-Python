from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente


cp = ContaPoupanca(123456, 654321, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

print("==================================================")

cc = ContaCorrente(246810, 108642, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
