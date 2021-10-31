# Calculadora de Cupons

from types import SimpleNamespace


cuponsFreeTotalDoMes = 6463
mensal = 4650


metaUsuario = int(input("Qual sua meta de cupons? "))
cuponsNoMomento = int(input("Quantos cupons você possui no momento? "))
mensalUsuario = int(input("Por favor, informe a quantidade de mensal que colocará nesse tempo: "))

#============================================================================#

valorQueFaltaParaMeta = metaUsuario - cuponsNoMomento
valorMensalUsuario = mensal * mensalUsuario
cuponsTotais = cuponsFreeTotalDoMes + valorMensalUsuario
mesTotal = valorQueFaltaParaMeta // cuponsTotais
if mesTotal == 1:
    print("Você pegará a quantia desejada em ", mesTotal, " mês!")

else:
    print("Você pegará a quantia desejada em ", mesTotal, " meses!")

#============================================================================#

quantidadeCupom = (cuponsTotais * mesTotal) + cuponsNoMomento
print("Você terá ao todo ", quantidadeCupom, " cupons!")



