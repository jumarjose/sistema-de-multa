from datetime import datetime, timedelta

# Pede para o usuário digitar a data
data_input = input("Digite a data do ocorrido no formato dd/mm/aaaa: ")

# Converte a string digitada para um objeto datetime
data_inicial = datetime.strptime(data_input, "%d/%m/%Y")

# Pede a quantidade de dias a somar
dias = 20

# Cria o intervalo e soma à data
nova_data = data_inicial + timedelta(days=dias)

# Mostra o resultado

velo = float(input('qual a velocidade do carro:'))
if velo <= 80:
    print('tudo ok')
elif velo > 80:
    print("vece esta multado")
    multa = (velo-80)*7
print('você esta a mais de oitenta km por hora sua multa e de {} e voce possui ate o dia {} para efetuar o pagamento'.format(multa, nova_data))


