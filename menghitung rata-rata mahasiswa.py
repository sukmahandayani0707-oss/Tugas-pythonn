mahasiswa = {
    "10121001": "Asep",
    "10121002": "Budi",
    "10121003": "Cecep"
}

nilai = {
    "10121001": [50, 70, 40, 80],
    "10121002": [78, 78, 80, 65],
    "10121003": [57, 88, 67, 69]
}

mata_kuliah = ["MK1", "MK2", "MK3", "MK4"]
rata_rata_mahasiswa = {}
for nim, daftar_nilai in nilai.items():
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    rata_rata_mahasiswa[nim] = rata_rata

nim_terpintar = max(rata_rata_mahasiswa, key=rata_rata_mahasiswa.get)
nilai_terpintar = rata_rata_mahasiswa[nim_terpintar]

jumlah_mk = len(mata_kuliah)
rata_rata_mk = [0] * jumlah_mk

for daftar_nilai in nilai.values():
    for i in range(jumlah_mk):
        rata_rata_mk[i] += daftar_nilai[i]

for i in range(jumlah_mk):
    rata_rata_mk[i] /= len(nilai)

indeks_terkecil = rata_rata_mk.index(min(rata_rata_mk))
mk_terkecil = mata_kuliah[indeks_terkecil]
nilai_terkecil = rata_rata_mk[indeks_terkecil]

print(f"Mahasiswa Terpintar : {mahasiswa[nim_terpintar]} (Nilai : {nilai_terpintar:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {mk_terkecil} (Nilai : {nilai_terkecil:.2f})")
