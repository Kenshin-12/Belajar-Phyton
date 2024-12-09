buku = []

def tampil_data():
    if len(buku) <= 0:
        print("DATA MASIH KOSONG")
    else:
        for i in range(len(buku)):
            print("%d %s" % (i, buku[i]))

def tambah_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

def ubah_data():
    tampil_data()
    i = int(input("Input ID buku : "))
    if( i > len(buku))  :
        print("input ID salah")
    else:
        judul_baru  = input("Judul baru : ")
        buku[i] = judul_baru

def hapus_data():
    tampil_data()
    i = int(input("Input ID buku : "))
    if(i > len(buku)):
        print("ID SALAH")
    else:
        buku.remove(buku[1])

def tampil_menu():
    print("\n")
    print("==========Menu===============")
    print("(1) Tampil data")
    print("(2) Tambah data")
    print("(3) Ubah data")
    print("(4) Hapus data")
    print("(5) Keluar")

    menu = int(input("pilih menu : "))
    print("\n")

    if menu == 1:
        tampil_data()
    elif menu == 2:
        tambah_data()
    elif menu == 3:
        ubah_data()
    elif menu == 4:
        hapus_data()
    elif menu == 5:
        exit()
    else:
        print("Salah pilih")


if __name__ == "__main__":
    while(True):
        tampil_menu() 
     
