# Program Python untuk menampilkan semua 
from itertools import combinations 

# Mendapatkan kombinasi dari [1, 1, 3] 
# dan panjang 2 
comb = combinations([1, 1, 3], 2) 

# Menampilkan kombinasi 
for i in comb: 
    print(i) 
