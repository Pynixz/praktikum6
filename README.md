### PRAKTIKUM6
# Subrutin:
- Subrutin adalah bagian kecil dari program yang dapat dipanggil untuk melakukan tugas tertentu.
- Digunakan untuk mengorganisir dan memecah program menjadi bagian-bagian yang lebih kecil dan mudah dikelola.
- Biasanya dipanggil dari bagian utama program (main program) dan dapat mengembalikan hasil ke pemanggilnya.
- Meningkatkan keterbacaan dan perawatan program.
# Fungsi:
- Fungsi adalah blok kode yang dirancang untuk melakukan tugas tertentu dan dapat dipanggil dari bagian manapun dalam program.
- Sama seperti subrutin, fungsi membantu dalam memecah program menjadi bagian-bagian yang lebih kecil dan terorganisir.
- Fungsi dapat mengembalikan nilai kepada pemanggilnya.
- Meningkatkan modularitas dan reusabilitas kode

### Codingan Program praktikum6
``` py
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
```
# Penjelasan
1. **Inisialisasi Daftar Nilai (`daftar_nilai`)**
   - Variabel `daftar_nilai` diinisialisasi sebagai list kosong untuk menyimpan data mahasiswa dalam bentuk kamus.

2. **Fungsi `tambah()`**
   - Meminta pengguna untuk memasukkan nama dan nilai mahasiswa.
   - Melakukan validasi menggunakan loop `while` dan `try-except` untuk memastikan nilai yang dimasukkan adalah angka.
   - Membuat kamus (`mahasiswa`) yang berisi nama dan nilai.
   - Menambahkan kamus tersebut ke dalam `daftar_nilai`.
   - Memberikan pesan konfirmasi bahwa data mahasiswa berhasil ditambahkan.

3. **Fungsi `tampilkan()`**
   - Menampilkan daftar mahasiswa dengan nama dan nilai mereka.
   - Menggunakan loop `for` untuk iterasi melalui setiap elemen dalam `daftar_nilai`.
   - Mencetak nama dan nilai setiap mahasiswa dengan nilai yang sudah dibulatkan ke bilangan bulat.

4. **Fungsi `hapus(nama)`**
   - Menerima parameter `nama` untuk menentukan mahasiswa yang akan dihapus.
   - Iterasi melalui `daftar_nilai` untuk mencari mahasiswa dengan nama yang sesuai.
   - Jika ditemukan, mahasiswa tersebut dihapus dari `daftar_nilai`.
   - Memberikan pesan konfirmasi bahwa data mahasiswa berhasil dihapus.

5. **Fungsi `ubah(nama)`**
   - Menerima parameter `nama` untuk menentukan mahasiswa yang akan diubah.
   - Iterasi melalui `daftar_nilai` untuk mencari mahasiswa dengan nama yang sesuai.
   - Jika ditemukan, pengguna diminta untuk memasukkan nilai baru, dan nilai mahasiswa diubah.
   - Memberikan pesan konfirmasi bahwa data mahasiswa berhasil diubah.

6. **Loop Utama (`while True`)**
   - Menampilkan menu utama kepada pengguna dengan opsi 1 hingga 5.
   - Meminta pengguna untuk memilih opsi.
   - Berdasarkan pilihan pengguna, program akan memanggil fungsi yang sesuai atau keluar dari loop jika opsi keluar dipilih.
   - Menangani situasi di mana pengguna memasukkan opsi yang tidak valid.

7. **Selesai**
   - Program mencetak "Program selesai. Sampai jumpa!" dan keluar dari program.

Penjelasan ini memberikan pemahaman mendalam tentang setiap aspek program, fungsi, dan cara program berinteraksi dengan pengguna serta melakukan manipulasi data pada `daftar_nilai`.

# OUTPUT


    - Hasil Inisialisasi Daftar Nilai
![Screenshot 2023-12-02 213705](https://github.com/Pynixz/praktikum6/assets/147568964/afae8fb0-9fc7-414d-b551-3ab21af7ce78)


    - Hasil Tambah data
![Screenshot 2023-12-02 211306](https://github.com/Pynixz/praktikum6/assets/147568964/44022dcb-f923-4efa-b9d1-ab2485b8f3b5)


    - Hasil Tampilkan Data
![Screenshot 2023-12-02 211254](https://github.com/Pynixz/praktikum6/assets/147568964/2f2c0b61-13d5-44c0-adf4-b072670f623a)


    - Hasil Hapus Data
![Screenshot 2023-12-02 211334](https://github.com/Pynixz/praktikum6/assets/147568964/0f0b71c6-c0f2-4317-94a8-539c4540f157)


    - Hasil Ubah Data
![Screenshot 2023-12-02 211358](https://github.com/Pynixz/praktikum6/assets/147568964/f122e561-3859-4619-b4f9-0ac378edd32d)


    - END / Keluar
![Screenshot 2023-12-02 211424](https://github.com/Pynixz/praktikum6/assets/147568964/684794ca-e5de-464c-ae4d-6afa9b7a247a)
