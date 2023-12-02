# Inisialisasi daftar nilai mahasiswa
daftar_nilai = []

# Fungsi tambah() untuk menambah data
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    while True:
        try:
            nilai = float(input("Masukkan nilai mahasiswa: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    mahasiswa = {"nama": nama, "nilai": nilai}
    daftar_nilai.append(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan.")

# Fungsi tampilkan() untuk menampilkan data
def tampilkan():
    print("Daftar Nilai Mahasiswa:")
    print("======================")
    for mahasiswa in daftar_nilai:
        nilai_tanpa_desimal = int(mahasiswa['nilai'])
        print(f"Nama: {mahasiswa['nama']}, Nilai: {nilai_tanpa_desimal}")

# Fungsi hapus(nama) untuk menghapus data berdasarkan nama
def hapus(nama):
    for mahasiswa in daftar_nilai:
        if mahasiswa["nama"] == nama:
            daftar_nilai.remove(mahasiswa)
            print(f"Data mahasiswa {nama} berhasil dihapus.")
            return
    print(f"Data mahasiswa {nama} tidak ditemukan.")

# Fungsi ubah(nama) untuk mengubah data berdasarkan nama
def ubah(nama):
    for mahasiswa in daftar_nilai:
        if mahasiswa["nama"] == nama:
            while True:
                try:
                    nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
                    break
                except ValueError:
                    print("Input tidak valid. Masukkan angka.")
            mahasiswa["nilai"] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.")
            return
    print(f"Data mahasiswa {nama} tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama_hapus = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama_hapus)
    elif pilihan == "4":
        nama_ubah = input("Masukkan nama mahasiswa yang akan diubah: ")
        ubah(nama_ubah)
    elif pilihan == "5":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")