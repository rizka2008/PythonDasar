# Membaca input nama dan gaji pokok
nama = input("Masukkan nama: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Menghitung tunjangan (20% dari gaji pokok)
tunjangan = 0.20 * gaji_pokok

# Menghitung pajak (15% dari total gaji)
pajak = 0.15 * (gaji_pokok + tunjangan)

# Menghitung gaji bersih
gaji_bersih = gaji_pokok + tunjangan - pajak

# Menampilkan hasil
print("Nama:", nama)
print("Gaji Pokok:", gaji_pokok)
print("Gaji Bersih:", gaji_bersih