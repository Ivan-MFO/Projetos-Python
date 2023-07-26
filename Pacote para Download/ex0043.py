#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: Abaixo de 18.5: Abaixo do peso, Entre 18.5 a 25: Peso ideal, Entre 25 até 30: Sobrepeso, de 30 á 40: Obesidade, Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')