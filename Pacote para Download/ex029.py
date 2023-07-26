# Escreva um progrma que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem  dizendo que ele foi multado. A multa custa R$ 7,00 por cada km acima do limite de velocidade

velocidade = float(input('Digite a velocidade do veículo: '))
multa = (velocidade - 80) * 7
print ('O limite da via é de 80km/h')

if velocidade <= 80:
    print ('Seguro! Você está dentro do limite de velocidade da via ')
if velocidade > 80:
    print ('MULTADO! Você esta acima do limite de velocidade da via ')
    print ('O valor da sua multa é de: R$ {:.2f}'.format(multa))
