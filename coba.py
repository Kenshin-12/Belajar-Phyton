class Pengiriman:
  def __init__(self, kode, kota_tujuan, berat):
    self.kode = kode
    self.kota_tujuan = kota_tujuan
    self.berat = berat
    self.tarif = self.hitung_tarif()

  def hitung_tarif(self):
    tarif = 0
    if self.kode == 1:  # Bandung
      if self.berat >= 100:
        tarif = 40000
      elif self.berat >= 40:
        tarif = 20000
      else:
        tarif = 10000
    elif self.kode == 2:  # Semarang
      if self.berat >= 100:
        tarif = 75000
      elif self.berat >= 40:
        tarif = 30000
      else:
        tarif = 20000
    elif self.kode == 3:  # Yogyakarta
      if self.berat >= 100:
        tarif = 80000
      elif self.berat >= 40:
        tarif = 40000
      else:
        tarif = 30000
    return tarif

  def hitung_total(self):
    pajak = self.tarif * 0.1
    total_harga = self.tarif + pajak
    return total_harga

# Input data pelanggan
nama_pelanggan = input("Nama Pelanggan: ")
tanggal_kirim = input("Tanggal Kirim: ")
jumlah_barang = int(input("Jumlah Barang: "))

# Data pengiriman dalam array
data_pengiriman = []

# Input data pengiriman per barang
for i in range(jumlah_barang):
  print(f"\nBarang ke-{i+1}:")
  kode = int(input("Kode Kota Tujuan (1-3): "))
  kota_tujuan = ""
  if kode == 1:
    kota_tujuan = "Bandung"
  elif kode == 2:
    kota_tujuan = "Semarang"
  elif kode == 3:
    kota_tujuan = "Yogyakarta"
  else:
    print("Kode kota tujuan tidak valid.")
    continue  # Lanjutkan ke iterasi berikutnya

  berat = float(input("Berat Barang (kg): "))

  pengiriman = Pengiriman(kode, kota_tujuan, berat)
  data_pengiriman.append(pengiriman)

# Menghitung total harga dan pajak
total_harga = 0
for pengiriman in data_pengiriman:
  total_harga += pengiriman.tarif

pajak = total_harga * 0.1
total_bayar = total_harga + pajak

# Menampilkan faktur pengiriman
print("\nFaktur Pengiriman Barang")
print("-------------------------")
print("Nama Pelanggan:", nama_pelanggan)
print("Tanggal Kirim:", tanggal_kirim)
print("Jumlah Barang:", jumlah_barang)
print("\nNo  Kota Tujuan  Berat  Harga")
print("-----------------------------")
no = 1
for pengiriman in data_pengiriman:
  print(f"{no}   {pengiriman.kota_tujuan:<12} {pengiriman.berat:<5} {pengiriman.tarif}")
  no += 1
print("-----------------------------")
print(f"Total Harga     = Rp {total_harga}")
print(f"Pajak          = Rp {pajak}")
print(f"Total Bayar     = Rp {total_bayar}")