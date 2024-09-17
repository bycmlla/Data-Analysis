from datetime import datetime, date, timedelta

dt = datetime(2024, 9, 12, 12, 55, 10)

print(dt.day)

strHour = dt.strftime('%d/%m/%Y %H:%M')

print(strHour)


# Criando um timedelta de 10 dias
delta = timedelta(days=10)

# Adicionando 10 dias à data atual
data_futura = dt + delta
print(data_futura)
