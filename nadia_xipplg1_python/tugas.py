# Fungsi untuk menghitung volume tabung
def hitung_volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

# Fungsi untuk menghitung volume balok
def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

# Input dari pengguna
pilihan = input("Pilih bentuk (tabung/balok): ")

if pilihan == "tabung":
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    volume_tabung = hitung_volume_tabung(jari_jari, tinggi)
    print(f"Volume tabung adalah {volume_tabung:.2f} satuan kubik")
elif pilihan == "balok":
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume_balok = hitung_volume_balok(panjang, lebar, tinggi)
    print(f"Volume balok adalah {volume_balok:.2f} satuan kubik")
else:
    print("Pilihan tidak valid. Silakan pilih 'tabung' atau 'balok'.")