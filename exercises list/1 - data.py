#Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro

from datetime import date, timedelta

dataAtual = date.today()

dataFutura = dataAtual + timedelta(days=2)

print(dataAtual)
print(dataFutura)
