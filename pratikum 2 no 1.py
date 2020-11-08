def luasSegitiga (alas, tinggi):
    luas  = alas * tinggi / 2
    luas2 = alas2 * tinggi2 / 2
    return luas

alas = 10
tinggi = 20
alas2 = 15
tinggi2 = 45
print('Luas segitiga dg alas', alas,
      ' dan tinggi', tinggi,
      ' adalah', luasSegitiga(alas, tinggi))
print('Luas segitiga dg alas', alas2,
      ' dan tinggi', tinggi2,
      ' adalah', luasSegitiga(alas2, tinggi2))
