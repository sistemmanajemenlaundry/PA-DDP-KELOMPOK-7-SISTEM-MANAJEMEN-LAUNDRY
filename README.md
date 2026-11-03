

# Laundry Management System
<p align="center">
<b>Tugas Akhir Pengantar Teknologi Informasi — Sistem Informasi UNMUL</b>

<p align="center">
  <b>Aplikasi CLI Pengelolaan Transaksi dan Invetaris Laundry Berbasis Python</b>
</p>

---

</div>

## 1. Judul & Tema

* **Nama Proyek:** Laundry Management System (LMS)
* **Tema:** Sistem Informasi Pengelolaan Jasa Laundry dan Invetaris Layanan Berbasis Command Line Interface (CLI).
* **Teknologi:** Python, JSON, PrettyTable, PWInput.

---

## 2. Anggota Kelompok & Peran

| Nama Anggota | NIM | Peran & Tanggung Jawab | GitHub |
| :---: | :--- | :---: | :--- |
| **Shafa Aurellia Rufina Maharani** | `2609116001` | Peran| @shafarufina8 (https://github.com/shafarufina8) |
| **Nazwa Dwi Amelia Putri** | `2609116008` | Peran | @ameapples (https://github.com/ameapples) |
| **Deboraa Lintang Apsari** | `2609116011` | Peran | @deboralintangapsari (https://github.com/deboralintangapsari) 
| **Raihanum Athaya Rana Insyra** | `2609116014` | Peran | @raihanumathaya(https://github.com/raihanumathaya) |

---

## 3. Deskripsi & Tujuan

### Deskripsi Proyek
**Laundry Management System** adalah aplikasi berbasis CLI yang dirancang untuk mempermudah manajemen operasional usaha laundry. Aplikasi ini mendukung autentikasi multi-role (Admin & Customer), pencatatan transaksi, pengelolaan paket laundry, serta penyimpanan data yang terstruktur menggunakan format JSON.

### Tujuan Utama
1. **Efisiensi Transaksi:** Mempercepat proses pencatatan dan perhitungan total biaya laundry.
2. **Manajemen Data:** Menyediakan sistem *Create, Read, Update, Delete* (CRUD) data layanan dan paket secara *real-time*.
3. **Keamanan & Peran:** Membatasi akses fitur sesuai dengan role pengguna (*Multi-role access*).

---

## 4. Flowchart System

Berikut adalah alur logika utama dari sistem yang dijalankan: <br>
1. Halaman Utama <br>

<img width="1487" height="962" alt="AdobeExpressPhotos_466d4e0ce6c345dd95fc6f7bf356a57f_CopyEdited" src="https://github.com/user-attachments/assets/05ca4714-b619-4be5-a4d4-04f49a5c24f2" /> <br>

Flowchart ini menampilkan menu utama, disini terdapat 3 pilihan (Login, Registrasi, Keluar), jika memilih selain dari opsi yang ada maka sistem akan menampilkan pesan "Pilihan tidak valid" dan kembali ke menu utama <br>

`Menu Login`<br>

Pengguna akan diminta untuk memasukkan Username dan Password, sistem akan membaca data dari file json dan memvalidasi apakah akun ada atau tidak, jika aku tidak valid maka program akan menampilkan pesan "Akun tidak valid" dan user akan kembali ke menu utama, jika akun valid, maka sistem akan mengecek peranan user tersebut, jika dia adalah admin maka dia akan masuk kedalam menu admin, dan jika dia adalah user maka dia akan masuk ke menu user.<br>

`Fitur Registrasi`<br>

User akan memasukkan username baru, sistem akan mengecek apakah username tersebut sudah ada atau belum, jika sudah ada maka program akan menampilkan "Username sudah terdaftar" dan diminta untuk memasukkan ulang, jika belum ada, user akan memasukkan password dan akun akan ditambahkan ke user.json<br>

`Fitur Keluar`<br>

Memilih menu keluar maka program akan di akhiri (end)

2. Menu Admin <br>

<img width="2051" height="1072" alt="PA-07-DDP-Menu Admin drawio (7)" src="https://github.com/user-attachments/assets/f0d49912-876a-45f6-a7f9-99b4b04de33d" /> <br>

Setelah berhasil login sebagai admin, sistem akan menampilkan menu admin yaitu Manajemen Layanan, Manajemen Pelanggan, Manajemen Top Up, Laporan Keuangan dan Logout Admin <br>

Setiap pilihan akan masuk kedalam konektor nya masing masing, dan apabila admin tidak memilih opsi yang ada maka program akan menampilkan "Pilihan tidak valid" <br>

3. CRUD Admin <br>

<img width="1441" height="1201" alt="PA-07-DDP-CRUD Admin drawio (4)" src="https://github.com/user-attachments/assets/ac023909-d32c-490f-b6ad-0aff291f5a31" /> <br>

`Proses Read` <br>

Sistem akan membaca seluruh data dari file json dan program akan menampilkan layanan yang ada.<br>
`Proses Create` <br>
Pengguna akan memasukkan data baru, lalu program akan memvalidasi, jika tidak valid maka program akan menampilkan "Input Tidak Valid", dan meminta untuk memasukkan data baru, jika valid maka progra  


4. Menu User <br>
<img width="1600" height="1392" alt="image" src="https://github.com/user-attachments/assets/73f91480-c4c9-4203-86ba-a3eeca18cb11" />

# Alur Panduan Penggunaan Program
## 1. Penggunaan Library dan Modul<br>
<img width="1330" height="252" alt="image" src="https://github.com/user-attachments/assets/0947037c-ea84-4e62-8e4f-0b8ac52b05a9" /><br>

Di awal program ini kami menggunakan beberapa library bawaan Python dan juga tambahannya seperti os, json, time, random, pwinput, dan prettytable. Os berfungsi untuk mengecek keberadaan file dan membersihkan tampilan terminal agar lebih rapi. Json digunakan untuk membaca dan menulis data dalam format JSON, sehingga data user, saldo, dan transaksi tetap tersimpan meskipun program ditutup. Time digunakan untuk memberi jeda antar tampilan menu dan mencatat waktu, sedangkan random untuk menghasilkan kode acak seperti ID transaksi. Pwinput berfungsi mengubah karakter password menjadi tanda bintang agar lebih aman. Terakhir, prettytable digunakan untuk menampilkan data dalam bentuk tabel yang lebih rapi dan mudah dibaca.<br>

## 2. Penggunaan Function Pendukung<br>
### Function Load dan Save ke File JSON
<img width="1022" height="732" alt="image" src="https://github.com/user-attachments/assets/cf210a32-69e1-47b3-9aae-4fb080c24681" /><br>
Fungsi load_json digunakan untuk membaca data dari file JSON, seperti transaksi, layananm dan top-up. Jika file tidak ditemukan atau isinya rusak, program menampilkan pesan error dan ngembalikan list kosong agar program tidak berhenti. Fungsi save_json digunakan untuk menyimpan data ke file JSON dengan format rapi (indent=4) dan dilengkapi try-except untuk menaampilkan pesan jika penyimpanan gagal. fungsi load_user bekerja seperti load_json, tetapi khusus untuk file users.json<br>
### Function Load User, Save User, Cari User<br>
<img width="852" height="854" alt="image" src="https://github.com/user-attachments/assets/68f04127-3ec4-4368-ba3a-5e3330b44f48" /><br> 
- load_user : membaca data semua pengguna dari file users.json, dan mengembalikanya dalam bentuk list. Jika file tidak ditemukan atau isinya rusak, program menampilkan pesan error. Fungsi ini dipakai saat login, registrasi, dan top-up untuk mengambil daftar user yang sudah terdaftar.<br>
- cari_user : mencari satu user dari daftar berdasarakan username. Fungsi ini menelusuri list satu persatu, dan kalau username cocok, hasilnya None. Fungsi ini dipakai untuk mengambil data untuk mengambil data dan saldo pengguna saat top-up, order, dan menampilkan menu user. <br>
- save_users : mencari data pengguna ke users.json dengan format rapi (indent=4). Fungsi ini dipanggil setiap ada perubahan, misalnya saat ada akun baru yang mendaftar atau saldo bertambah setelah top-up. Ada try-except juga supaya kalau penyimpanan gagal, program menampilkan pesan dan tidak langsung berhenti.<br>
## 3. Function Menu Utama 
Fungsi ini membersikan layar lalu menampilkan tampilan menu utama dengan tiga pilihan menu yaitu login, registrasi, dan  keluar. Di bawahnya ada perulangan while True yang terus menampilkan menu dan membaca pilihan pengguna. Pilihan 1 memanggil login(), pilihan 2 memanggil regis(), dan pilihan 3 mencetak "terima kasih!" lalu break ntuk menghentikan program. Input selain itu menampilkan pesan tidak valid.




























