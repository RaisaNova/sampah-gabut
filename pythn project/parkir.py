import datetime

plat_nomor = input("silahkan masukkan plat nomor anda :")

print(f"plat nomor anda {plat_nomor}")

class Kendaraan:
    def _init_(self, plat_nomor):
        self.plat_nomor = plat_nomor
        self.waktu_masuk = datetime.datetime.now()

    def hitung_durasi(self):
        waktu_keluar = datetime.datetime.now()
        durasi = waktu_keluar - self.waktu_masuk
        durasi_jam = durasi.total_seconds() // 3600
        return durasi_jam

class Parkir:
    def _init_(self, tarif_per_jam=2000):
        self.kendaraan_parkir = {}
        self.tarif_per_jam = tarif_per_jam

    def masuk(self, plat_nomor):
        if plat_nomor in self.kendaraan_parkir:
            print(f"Kendaraan dengan plat {plat_nomor} sudah parkir.")
        else:
            kendaraan = Kendaraan(plat_nomor)
            self.kendaraan_parkir[plat_nomor] = kendaraan
            print(f"Kendaraan dengan plat {plat_nomor} berhasil masuk.")

    def keluar(self, plat_nomor):
        if plat_nomor not in self.kendaraan_parkir:
            print(f"Kendaraan dengan plat {plat_nomor} tidak ditemukan.")
        else:
            kendaraan = self.kendaraan_parkir.pop(plat_nomor)
            durasi = kendaraan.hitung_durasi()
            biaya = durasi * self.tarif_per_jam
            print(f"Kendaraan dengan plat {plat_nomor} keluar.")
            print(f"Durasi parkir: {durasi:.1f} jam")
            print(f"Biaya parkir: Rp {biaya}")

    def tampilkan_kendaraan_parkir(self):
        if not self.kendaraan_parkir:
            print("Tidak ada kendaraan yang sedang parkir.")
        else:
            print("Kendaraan yang sedang parkir:")
            for plat in self.kendaraan_parkir:
                print(f"- Plat nomor: {plat}")

# Fungsi utama untuk menjalankan aplikasi
def main():
    parkir = Parkir()
    while True:
        print("\n=== Aplikasi Parkir ===")
        print("1. Masukkan kendaraan")
        print("2. Keluarkan kendaraan")
        print("3. Tampilkan kendaraan yang sedang parkir")
        print("4. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            plat_nomor = input("Masukkan plat nomor kendaraan: ")
            parkir.masuk(plat_nomor)
        elif pilihan == "2":
            plat_nomor = input("Masukkan plat nomor kendaraan: ")
            parkir.keluar(plat_nomor)
        elif pilihan == "3":
            parkir.tampilkan_kendaraan_parkir()
        elif pilihan == "4":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "_main_":
    main()