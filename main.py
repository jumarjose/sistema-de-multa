from datetime import datetime, timedelta

data_input = input("Digite a data do ocorrido no formato dd/mm/aaaa: ")
data_inicial = datetime.strptime(data_input, "%d/%m/%Y")
dias = 20
nova_data = data_inicial + timedelta(days=dias)
velo = float(input('qual a velocidade do carro:'))
if velo <= 80:
    print('tudo ok')
elif velo > 80:
    print("vece esta multado")
    multa = (velo-80)*7
print('você esta a mais de oitenta km por hora sua multa e de {} e voce possui ate o dia {} para efetuar o pagamento'.format(multa, nova_data))



