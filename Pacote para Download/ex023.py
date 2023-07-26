#Faça um programa que leia um número do 0 ao 9999 e mostre na tela cada um dos dígitos separados, un, de, cen, mi

num = int(input('Digite um número de 0 à 9999: '))
#n = str(num)
#print ('Analizando seu número {}'.format(num))
#print ('Seu número possui {} unidades'.format(n[3]))
#print ('Seu número possui {} dezenas'.format(n[2]))
#print ('Seu número possui {} centenas'.format(n[1]))
#print ('Seu número possui {} milhares'.format(n[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('Após análise do número ele possui {}'.format(num))
print ('Unidades: {}'.format(u))
print ('Dezenas: {}'.format(d))
print ('Centenas: {}'.format(c))
print ('Milhares: {}'.format(m))
