

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










