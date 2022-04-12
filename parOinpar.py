num = float(input('Ingrese su numero a consultar'))

res = int(num/2) - (num / 2)

if res == 0:
    print('El numero ' + str(num) + ' es par')
else:
    print('El numero no es par')