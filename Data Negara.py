import os
import random
import string\

data = dict()

while True:
    os.system("cls")  
    print(f"{'DATA NEGARA':^40}")
 
    keyFinal = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    nama_negara = input("Enter Nama Negara\t: ")
    ibu_kota = input("Enter Ibu Kota\t\t: ")
    benua = input("Enter Benua\t\t: ")
    
    data[keyFinal] = {
        'namakey': nama_negara,
        'ibukotakey': ibu_kota,
        'benuakey': benua
    }
    
    opsi = input("Input data Lagi (y/t) : ").lower()
    if opsi == 't':
        break

print("-" * 40)
print(f"{'Key':<5} {'Nama Negara':<20} {'Ibu Kota':<15} {'Benua':<15}")
print("-" * 40)

for key, value in data.items():
    print(f"{key:<5} {value['namakey']:<20} {value['ibukotakey']:<15} {value['benuakey']:<15}")