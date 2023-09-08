# Membaca bilangan dari pengguna
bilangan = int(input("Masukkan sebuah bilangan: "))

# Memeriksa apakah bilangan genap atau ganjil
if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")