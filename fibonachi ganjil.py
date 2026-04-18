def hitung_pangkat(bilangan, pangkat):
    return bilangan ** pangkat

def hitung_pecahan():
    hasil = 1 - 2/3 + 5/8 - 13/21
    return hasil

print("1. A pangkat B")
print("2. Hitung 1 - 2/3 + 5/8 - 13/21 +")
print("0. keluar")

pilihan = input("Masukkan pilihan Anda: ")

if pilihan == '1':
    bilangan = int(input("masukan suatu bilangan bulat :"))
    pangkat = int(input("masukan pangkat yang diinginkan : "))
    for i in range(1, pangkat + 1):
        hasil = hitung_pangkat(bilangan, i)
        print(f"hasil {bilangan} pangkat {i} adalah {hasil}")
elif pilihan == '2':
    hasil = hitung_pecahan()
    print(f"Hasil perhitungan pecahan adalah: {hasil}")
elif pilihan == '0':
    print("Keluar dari program.")
else:
    print("Pilihan tidak valid.")

n = int(input("Masukkan jumlah N : "))
if n == 2:
    print(0.3333333)