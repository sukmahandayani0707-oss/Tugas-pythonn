nama = ["Asep", "Budi", "Cecep"]


nilai = [
    [50, 70, 40, 80],   # Asep
    [78, 78, 80, 65],   # Budi
    [57, 88, 67, 69]    # Cecep
]

rata = [sum(n) / len(n) for n in nilai]
idx_terbaik = rata.index(max(rata))

print(f"Mahasiswa Terpintar: {nama[idx_terbaik]} ({rata[idx_terbaik]:.2f})")


rata_mk = [sum(n[i] for n in nilai) / len(nilai) for i in range(len(nilai[0]))]
idx_mk = rata_mk.index(min(rata_mk))

print(f"Mata Kuliah Nilai Terkecil: MK{idx_mk+1} ({rata_mk[idx_mk]:.2f})")