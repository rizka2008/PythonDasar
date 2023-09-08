# Definisika kelas dasar Vehicle
class Vehicle:
    def __init__(self, merk, tahun, warna):
        self.merk = merk 
        self.tahun = tahun 
        self.warna = warna

    def tampilan_info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Warna: {self.warna}")

# Definisikan kelas turunan Car yang mewarisi dari Vehicle 
class Car(Vehicle):
    def __init__(self, merk, tahum, warna, model):
        # Panggil konstruktor kelas dasar 
        super().__init__(merk, tahum, warna,)       
        self.model = model 

    def tampilan_info(self):
        # Pangil metode kelas dasar untuk menampilkan info kendaraan  
        super().tampilan_info()
        print(f"Model: {self.model}")

# Program utama 
if __name__=="__main__":
    car = Car("Toyota", 2022, "Merah", "Camry")

    print("Info Kendaraan:")
    car.tampilan_info()           