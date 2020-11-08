from operation import *
def jumlah(a, b):
    hasil = a + b
    return hasil

def kali(a, b):
    hasil = a * b
    return hasil

def kurang(a, b):
    hasil = a - b
    return hasil

def bagi(a, b):
    hasil = a / b
    return hasil
# soal a
a = jumlah(2, 4)
b = kurang(6, 4)
print(a, '*', b, '=', kali(a, b))

# soal b
a = jumlah(4, 7)
b = kurang(6, 9)
print(a, '*', b, '=', kali(a, b))

# soal c
a = jumlah(10, 2)
b = bagi(jumlah(7, 5),kurang(12, 34))
print(a, '/', b, '=', bagi(a, b))

