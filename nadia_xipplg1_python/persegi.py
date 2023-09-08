# Fungsi untuk menghitung luas dan keliling persegi panjang
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Fungsi untuk menghitung luas dan keliling trapesium
def hitung_trapesium(panjang_sisi_atas, panjang_sisi_bawah, tinggi):
    luas = 0.5 * (panjang_sisi_atas + panjang_sisi_bawah) * tinggi
    keliling = panjang_sisi_atas + panjang_sisi_bawah + (2 * (tinggi*2 + ((panjang_sisi_atas - panjang_sisi_bawah)/2)2)*0.5)
    return luas, keliling

# Input dari pengguna
panjang_persegi_panjang = float(input("Masukkan panjang persegi panjang: "))
lebar_persegi_panjang = float(input("Masukkan lebar persegi panjang: "))

panjang_sisi_atas_trapesium = float(input("Masukkan panjang sisi atas trapesium: "))
panjang_sisi_bawah_trapesium = float(input("Masukkan panjang sisi bawah trapesium: "))
tinggi_trapesium = float(input("Masukkan tinggi trapesium: "))

# Menghitung luas dan keliling persegi panjang
luas_persegi_panjang, keliling_persegi_panjang = hitung_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang)

# Menghitung luas dan keliling trapesium
luas_trapesium, keliling_trapesium = hitung_trapesium(panjang_sisi_atas_trapesium, panjang_sisi_bawah_trapesium, tinggi_trapesium)

# Menampilkan hasil
print("Luas persegi panjang: ", luas_persegi_panjang)
print("Keliling persegi panjang: ", keliling_persegi_panjang)

print("Luas trapesium: ", luas_trapesium)
print("Keliling trapesium: ", keliling_trapesium)