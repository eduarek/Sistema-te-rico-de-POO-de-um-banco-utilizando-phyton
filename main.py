class Main:
    pass

print("testando projeto")

from Cliente import Cliente
from Conta import Conta

c1= Cliente("João", "114444-2222")
conta= Conta(c1._nome, 6565, 0)

conta.deposita(100)
conta.saque(50)
conta.extrato()
print(conta.titular, "\nNúmero da Conta:", conta.numero, "\nSeu saldo: ", conta.saldo)
