kwiaty = ['konwalie', 'roze', 'bratki', 'stokrotki']
ilosc = [10, 51, 17, 35]
for idx in range( len(kwiaty)) :
    print("idx: " + str(idx) + ": " + kwiaty[idx])
    print(kwiaty[idx] + "ma ilosc kwiatow " + str(ilosc[idx]))
bratki = [100, 200, 70]
suma = [150]
suma = 0

for c in bratki:
    suma = suma + c
    print (suma)

if suma > 400:
   print('20% off, >400PLN!')
   suma = suma - (suma*20.0)/100
if len(kwiaty) > 3:
    print('000 Udane zakupy')
    suma = suma - (suma * 15.0) /100
    print("zaplac: {0}" .format(suma))
