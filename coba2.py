def hitung_harga_tiket(kode_pesawat):
  """Menghitung harga tiket berdasarkan kode pesawat."""
  if kode_pesawat == 1:
    nama_pesawat = "Garuda Indonesia"
    harga = 275000
  elif kode_pesawat == 2:
    nama_pesawat = "Mandala"
    harga = 230000
  elif kode_pesawat == 3:
    nama_pesawat = "Merpati"
    harga = 185000
  elif kode_pesawat == 4:
    nama_pesawat = "Lion Air"
    harga = 150000
  else:
    nama_pesawat = "Kode tidak valid"
    harga = 0
  return nama_pesawat, harga

# Input data
kode_pesawat = int(input("Masukkan kode pesawat (1-4): "))
jumlah_beli = int(input("Masukkan jumlah beli: "))
uang_bayar = int(input("Masukkan uang bayar: "))

# Hitung harga tiket
nama_pesawat, harga_tiket = hitung_harga_tiket(kode_pesawat)

# Hitung jumlah bayar, PPN, biaya bersih, dan kembalian
jumlah_bayar = harga_tiket * jumlah_beli
ppn = 0.1 * jumlah_bayar
biaya_bersih = jumlah_bayar + ppn
kembalian = uang_bayar - biaya_bersih

# Menampilkan output
print("\nDetail Pembelian Tiket Pesawat")
print("-------------------------------")
print("Nama Pesawat:", nama_pesawat)
print("Harga Tiket:", harga_tiket)
print("Jumlah Beli:", jumlah_beli)
print("Jumlah Bayar:", jumlah_bayar)
print("PPN (10%):", ppn)
print("Biaya Bersih:", biaya_bersih)
print("Uang Bayar:", uang_bayar)
print("Kembalian:", kembalian)