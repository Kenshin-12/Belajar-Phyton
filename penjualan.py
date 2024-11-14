import json

stok_barang = {}

def tambah_barang():
    """Fungsi untuk menambahkan barang baru."""
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        harga = float(input("Masukkan harga barang per unit: "))  # Tambahkan input harga
    except ValueError:
        print("Jumlah dan harga harus berupa angka. Silakan coba lagi.")
        return

    stok_barang[kode_barang] = {
        'nama_barang': nama_barang,
        'jumlah': jumlah,
        'harga': harga  # Simpan harga di dictionary
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
        print("Daftar Stok Barang:")
        for kode, data in stok_barang.items():
            print(f"Kode Barang: {kode}, Nama: {data['nama_barang']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
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

def menu_pembeli(barang):
    """Menu untuk pembeli memesan barang."""
    pesanan = {}
    
    # Tampilkan daftar barang yang tersedia
    print("\nDaftar Barang yang Tersedia:")
    if barang:
        for kode, data in barang.items():
            print(f"Kode Barang: {kode}, Nama: {data['nama_barang']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Stok kosong.")
    print("\n")

    while True:
        jenis = input("Masukkan kode barang yang ingin dibeli (atau ketik 'selesai' untuk selesai): ")
        if jenis.lower() == 'selesai':
            break
        if jenis not in barang:
            print("Barang tidak tersedia.")
            continue
        try:
            jumlah_beli = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        except ValueError:
            print("Jumlah harus berupa angka. Silakan coba lagi.")
            continue

        if jumlah_beli > barang[jenis]['jumlah']:
            print("Stok tidak mencukupi.")
            continue

        pesanan[jenis] = jumlah_beli
    return pesanan

def hitung_total(pesanan, barang):
    """Menghitung total harga pembelian."""
    total = 0
    for jenis, jumlah_beli in pesanan.items():
        harga_per_unit = barang[jenis]['harga']
        total += jumlah_beli * harga_per_unit
    return total

def pilih_mode():
    """Meminta user untuk memilih mode penjual atau pembeli."""
    while True:
        mode = input("Masuk sebagai (penjual/pembeli)? ").lower()
        if mode in ("penjual", "pembeli"):
            return mode
        else:
            print("Pilihan tidak valid. Silakan pilih 'penjual' atau 'pembeli'.")

def main():
    """Fungsi utama program."""
    print("Selamat datang di program penjualan dan pembelian!")
    print("-" * 30)

    # Muat data barang dari file jika ada
    try:
        with open('barang.txt', 'r') as f:
            stok_barang.update(json.load(f))
    except FileNotFoundError:
        pass  # Abaikan jika file tidak ditemukan

    while True:  # Loop utama program
        # Pilih mode user
        mode = pilih_mode()

        if mode == "penjual":
            def menu():
                while True:
                    print("=== Program Stock Opname ===")
                    print("1. Tambah Barang")
                    print("2. Update Stok")
                    print("3. Lihat Stok")
                    print("4. Hapus Barang")
                    print("5. Keluar")

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
                        print("Kembali ke menu utama.")
                        with open('barang.txt', 'w') as f:  # Simpan data barang ke file
                            json.dump(stok_barang, f)
                        return  # Keluar dari menu penjual
                    else:
                        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.\n")
            menu()

        elif mode == "pembeli":
            # Input pesanan dari pembeli
            pesanan = menu_pembeli(stok_barang)

            # Hitung total harga
            total_harga = hitung_total(pesanan, stok_barang)

            # Tampilkan ringkasan pesanan
            print("\nRingkasan Pesanan:")
            for jenis, jumlah_beli in pesanan.items():
                harga_per_unit = stok_barang[jenis]['harga']
                subtotal = jumlah_beli * harga_per_unit
                print(f"{jenis}: {jumlah_beli} x {harga_per_unit} = {subtotal}")
            print(f"Total Harga: {total_harga}")

if __name__ == "__main__":
    main()