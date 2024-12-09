import pandas as pd

stok_barang = {}
laporan_penjualan = []  # List untuk menyimpan laporan penjualan

def tambah_barang():
    """Fungsi untuk menambahkan barang baru."""
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        harga = float(input("Masukkan harga barang per unit: "))
    except ValueError:
        print("Jumlah dan harga harus berupa angka. Silakan coba lagi.")
        return

    stok_barang[kode_barang] = {
        'nama_barang': nama_barang,
        'jumlah': jumlah,
        'harga': harga
    }
    print(f"Barang '{nama_barang}' berhasil ditambahkan.\n")

def update_stok():
    """Fungsi untuk memperbarui jumlah stok barang."""
    kode_barang = input("Masukkan kode barang yang ingin diperbarui: ")
    if kode_barang in stok_barang:
        try:
            jumlah_baru = int(input("Masukkan jumlah stok terbaru: "))
        except ValueError:
            print("Jumlah harus berupa angka. Silakan coba lagi.")
            return
        stok_barang[kode_barang]['jumlah'] = jumlah_baru
        print(f"Stok barang '{stok_barang[kode_barang]['nama_barang']}' berhasil diperbarui.\n")
    else:
        print("Kode barang tidak ditemukan.\n")

def lihat_stok():
    """Fungsi untuk menampilkan daftar stok barang."""
    if stok_barang:
        data_barang = {
            "Kode Barang": [],
            "Nama Barang": [],
            "Jumlah": [],
            "Harga": []
        }
        for kode, data in stok_barang.items():
            data_barang["Kode Barang"].append(kode)
            data_barang["Nama Barang"].append(data['nama_barang'])
            data_barang["Jumlah"].append(data['jumlah'])
            data_barang["Harga"].append(data['harga'])

        df = pd.DataFrame(data_barang)
        print("\nDaftar Stok Barang:")
        print(df.to_markdown(index=False, tablefmt="grid"))
        print("\n")
    else:
        print("Stok kosong.\n")

def hapus_barang():
    """Fungsi untuk menghapus barang dari stok."""
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    if kode_barang in stok_barang:
        del stok_barang[kode_barang]
        print("Barang berhasil dihapus.\n")
    else:
        print("Kode barang tidak ditemukan.\n")

def menu_pembeli():
    """Menu untuk pembeli memesan barang."""
    pesanan = {}

    # Tampilkan daftar barang yang tersedia
    lihat_stok()

    while True:
        jenis = input("Masukkan kode barang yang ingin dibeli (atau ketik 'selesai' untuk selesai): ")
        if jenis.lower() == 'selesai':
            break
        if jenis not in stok_barang:
            print("Barang tidak tersedia.")
            continue
        try:
            jumlah_beli = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        except ValueError:
            print("Jumlah harus berupa angka. Silakan coba lagi.")
            continue

        if jumlah_beli > stok_barang[jenis]['jumlah']:
            print("Stok tidak mencukupi.")
            continue

        pesanan[jenis] = jumlah_beli

    total_harga = 0
    print("\nRingkasan Pesanan:")
    for jenis, jumlah_beli in pesanan.items():
        nama_barang = stok_barang[jenis]['nama_barang']
        harga_per_unit = stok_barang[jenis]['harga']
        subtotal = jumlah_beli * harga_per_unit
        total_harga += subtotal
        stok_barang[jenis]['jumlah'] -= jumlah_beli
        print(f"{nama_barang}: {jumlah_beli} x {harga_per_unit} = {subtotal}")

        # Tambahkan ke laporan penjualan
        laporan_penjualan.append({
            "Kode Barang": jenis,
            "Nama Barang": nama_barang,
            "Jumlah": jumlah_beli,
            "Subtotal": subtotal
        })
    print(f"Total Harga: {total_harga}")

def lihat_laporan_penjualan():
    """Fungsi untuk menampilkan laporan penjualan."""
    if laporan_penjualan:
        df = pd.DataFrame(laporan_penjualan)
        print("\nLaporan Penjualan:")
        print(df.to_markdown(index=False, tablefmt="grid"))
    else:
        print("Belum ada penjualan.\n")

def pilih_mode():
    """Meminta user untuk memilih mode penjual atau pembeli."""
    while True:
        print("\n1. Penjual")
        print("2. Pembeli")
        print("3. Lihat Laporan Penjualan")
        print("4. Keluar")
        mode = input("Pilih mode (1-4): ")
        if mode == '1':
            return "penjual"
        elif mode == '2':
            return "pembeli"
        elif mode == '3':
            return "laporan"
        elif mode == '4':
            print("Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

def main():
    """Fungsi utama program."""
    print("Selamat datang di program penjualan dan pembelian!")
    print("-" * 30)

    while True:
        mode = pilih_mode()

        if mode == "penjual":
            while True:
                print("\n=== Menu Penjual ===")
                print("1. Tambah Barang")
                print("2. Update Stok")
                print("3. Lihat Stok")
                print("4. Hapus Barang")
                print("5. Kembali ke Menu Utama")

                pilihan = input("Pilih menu (1-5): ")
                if pilihan == '1':
                    tambah_barang()
                elif pilihan == '2':
                    update_stok()
                elif pilihan == '3':
                    lihat_stok()
                elif pilihan == '4':
                    hapus_barang()
                elif pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.\n")

        elif mode == "pembeli":
            menu_pembeli()

        elif mode == "laporan":
            lihat_laporan_penjualan()

if __name__ == "__main__":
    main()
