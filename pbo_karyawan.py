class bidangKaryawan(object):
    jumlahkaryawan = 0
    totalGaji = 0

    def __init__(self, nama, gaji, status):
        self.nama = nama
        self.gaji = gaji
        self.status = status
        KaryawanPHOTOMAN.jumlahkaryawan += 1
        KaryawanPHOTOMAN.totalGaji += gaji

    def namaBidang(self):
        if self.status == 1:
            return "Dekorasi"
        elif self.status == 2:
            return "Foto"
        elif self.status == 3:
            return "Video"
        else:
            return "Editing"


class KaryawanPHOTOMAN(bidangKaryawan):
    @staticmethod
    def tampilkanJumlahKaryawan():
        print("Total Karyawan adalah", KaryawanPHOTOMAN.jumlahkaryawan, "orang")

    def tampilkanselfKaryawan(self):
        print("Nama Karyawan : ", self.nama)
        print("Gaji : Rp", self.gaji)
        print("Bidang : ", self.namaBidang())

    @staticmethod
    def tampilkanTotalGaji():
        print("Total Gaji dari beberapa karyawan adalah Rp", KaryawanPHOTOMAN.totalGaji)

    @staticmethod
    def tampilkanRataGaji():
        rataGaji = (KaryawanPHOTOMAN.totalGaji / KaryawanPHOTOMAN.jumlahkaryawan)
        print("Rata-rata Gaji dari beberapa karyawan adalah Rp", rataGaji)


# Program
emp1 = KaryawanPHOTOMAN("Iwan", 3000, 2)
emp1.tampilkanselfKaryawan()
emp2 = KaryawanPHOTOMAN("Adi", 4000, 1)
emp2.tampilkanselfKaryawan()

KaryawanPHOTOMAN.tampilkanJumlahKaryawan()
KaryawanPHOTOMAN.tampilkanTotalGaji()
KaryawanPHOTOMAN.tampilkanRataGaji()
