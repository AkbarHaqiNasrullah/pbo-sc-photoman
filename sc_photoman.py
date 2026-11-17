NAMA_BIDANG = {1: "Fotografer", 2: "Videografer", 3: "Editing", 4: "Dekorasi"}

class Karyawan:
  daftarKaryawan = []
  def __init__(self, nama, bidang):
    self.nama = nama
    self.bidang = bidang
    if bidang == 1:
      self.gaji = "1.000.000"
    elif bidang == 2:
      self.gaji = "2.000.000"
    elif bidang == 3:
      self.gaji = "2.500.000"
    elif bidang == 4:
      self.gaji = "1.500.000"

  def tambahKaryawan(self):
    self.dataKaryawan = [self.nama, self.bidang, self.gaji]
    Karyawan.daftarKaryawan.append(self.dataKaryawan)
    print("Data karyawan telah ditambahkan!")

def menu_utama():
  print("--------------- PILIH MENU ---------------")
  print("1. Input Data Karyawan")
  print("2. Check Data Karyawan")
  print("3. Hapus Data Karyawan")
  print("4. Keluar Program")
  print("")
  try:
    opsi = int(input("Pilihan : "))
  except ValueError as e:
    print(e)
    menu_utama()
    return

  if opsi == 1:
    in_nama = input("Masukkan Nama Karyawan : ")
    print("[1] Fotografer")
    print("[2] Videografer")
    print("[3] Editing")
    print("[4] Dekorasi")
    try:
      in_bidang = int(input("Masukkan Bidang Karyawan : "))
    except ValueError:
      in_bidang = 0
    if in_bidang not in [1,2,3,4]:
      print("Bidang Karyawan yang dimasukkan tidak tersedia")
      print("Tekan [ENTER] untuk kembali ke menu utama")
      input()
      menu_utama()
      return
    obj_Karyawan = Karyawan(in_nama, in_bidang)
    obj_Karyawan.tambahKaryawan()
    print("Tekan [ENTER] untuk kembali ke menu utama")
    input()
    menu_utama()
  elif opsi == 2:
    for karyawan in Karyawan.daftarKaryawan:
      print(f'Nama : {karyawan[0]}')
      print(f'Bidang : {NAMA_BIDANG[karyawan[1]]}')
      print(f'Gaji : {karyawan[2]}')
      print()
    print("Tekan [ENTER] untuk kembali ke menu utama")
    input()
    menu_utama()
  elif opsi == 3:
    in_nama = input("Masukkan Nama Karyawan : ")
    index = 0
    ketemu = False
    for nama in Karyawan.daftarKaryawan:
      if nama[0] == in_nama:
        ketemu = True
        break
      index += 1
    if ketemu == True:
      del Karyawan.daftarKaryawan[index]
      print("Data Karyawan Telah Dihapus")
    else:
      print("Data Karyawan tidak ditemukan")

    print("Tekan [ENTER] untuk kembali ke menu utama")
    input()
    menu_utama()
  elif opsi == 4:
      print("Program Telah Selesai...")
  else:
      print("Inputan Yang Anda Masukkan Salah!")
      menu_utama()


menu_utama()
