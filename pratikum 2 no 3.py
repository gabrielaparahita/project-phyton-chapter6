def luasSegitiga (alas, tinggi):
    luas  = alas * tinggi / 2
    luas2 = alas2 * tinggi / 2
    jumlah = luas + luas2
    print('Luas segitiga dg alas', alas, 'dan tinggi',tinggi,
          'adalah', luas)
    print('jumlah kedua luas tersebut', jumlah)
alas = 10
tinggi = 20
alas2 = 15
tinggi2 = 45
luasSegitiga(alas,tinggi)
luasSegitiga(alas2,tinggi2)
luasSegitiga(luas,luas2)
