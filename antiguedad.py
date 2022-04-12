ac = 1
log = 2
ger = 3


clave = int(input('Ingrese la clave de su departamento'))
antiguedad = int(input('Ingrese su antiguedad en la empresa'))

if clave == 1:
    if antiguedad == 1:
        print('tendras 6 dias de vacaciones')
    elif antiguedad >= 2 or antiguedad <= 6:
        print('tendras 14 dias de vacaciones')
    elif antiguedad >= 7 :
        print('tendras 20 dias de vacaciones')
elif clave == 2:
    if antiguedad == 1:
        print('tendras 7 dias de vacaciones')
    elif antiguedad >= 2 or antiguedad <= 6:
        print('tendras 15 dias de vacaciones')
    elif antiguedad >= 7 :
        print('tendras 22 dias de vacaciones')
elif clave == 3:
    if antiguedad == 1:
        print('tendras 10 dias de vacaciones')
    elif antiguedad >= 2 or antiguedad <= 6:
        print('tendras 20 dias de vacaciones')
    elif antiguedad >= 7 :
        print('tendras 30 dias de vacaciones')
else:
    print('Su codigo de departamento no existe ')