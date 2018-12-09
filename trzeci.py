produkt = 'mleko'
suma = 150
if 100 < suma and suma < 200:
    print ('Promocja 30%!')
    suma = suma - (suma * 30) / 100
elif suma >= 200:
    print ('promocja 35%')
    suma = suma - (suma * 35) / 100
else:
    print('bez promocji')
print('Do zaplacenia' + str(suma))
