

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

## 3. Function Menu Utama <br>

<img width="1354" height="858" alt="image" src="https://github.com/user-attachments/assets/c022eb1a-85a8-4885-a697-acfd4306f858" /><br>

Fungsi ini membersikan layar lalu menampilkan tampilan menu utama dengan tiga pilihan menu yaitu login, registrasi, dan  keluar. Di bawahnya ada perulangan while True yang terus menampilkan menu dan membaca pilihan pengguna. Pilihan 1 memanggil login(), pilihan 2 memanggil regis(), dan pilihan 3 mencetak "terima kasih!" lalu break ntuk menghentikan program. Input selain itu menampilkan pesan tidak valid.<br>

## 4. Function Login <br>

<img width="1308" height="1226" alt="image" src="https://github.com/user-attachments/assets/e55fd8fd-9181-4004-9386-de129e4b67f8" />
Fungsi ini memberi pengguna 3 kesempatan untuk login. Program meminta username dan password yang disembunyikan menggunakan pwinput yang kemudian dicocokan dengan data di users.json. jika cocok, program menampilkan pesan selamat datang dan mengarahkan sesuai roleh: admin ke admin() dan user ke menu_user(). Jika salah, kesempatan berkurang satu dan tersisa akan ditampilkan sampai habis.

## 5. Function Registrasi <br>

<img width="1036" height="1226" alt="image" src="https://github.com/user-attachments/assets/579b5fe0-0157-412c-a434-acd80c005133" />
<img width="700" height="480" alt="image" src="https://github.com/user-attachments/assets/da8d67c4-0436-4f29-88fa-81cc6b542cda" />
Fungsi ini membuat akun pelanggan baru. program memvalidasi bahwa username tidak kosong dan belum dipakai, password 4-8 karakter, serta nomor telepon berupa angka 10-13 digit. Jika semua valid, data baru ditambahkan dengan role user dan saldo awal 0, lalu disimpan ke users.json dengan save_users.

## 6. Function Menu User <br>
<img width="1326" height="1150" alt="image" src="https://github.com/user-attachments/assets/35a7f3b1-e23a-41e5-9a25-03b6b71f9747" /><br> 
Fungsi ini adalah menu utama setelah akun dengan role pelanggan berhasil login. Setiap kali menu tampil, program membaca ulang saldo terbaru dari users.json dan menampilkannya di bagian atas, menu memiliki 5 pilihan yaitu katalog Layanan, Top-Up Saldo, Order Laundry, Riwayat Transaksi, dan Logout. Pilihan 1-4 memanggil fungsi masing-masing dan kembali ke menu utama.<br>

## 7. Function Katalog Layanan<br>
<img width="1538" height="568" alt="image" src="https://github.com/user-attachments/assets/3f5fa965-13f5-4ce2-9dd1-a2ab16b303d3" /><br>
Fungsi tampilan_katalog dan katalog_layanan adalah untuk menampilkan daftar layanan dalam bentuk tabel PrettyTable dengan kolom ID, Nama, Kategori, Harga (berformat Rp), dan estimasi. Fungsi katalog membaca layanan.json, lalu memeanggil tampilan katalog jika data ada, atau menampilkan "Belum ada layanan" jika kosong. Fungsi tampilan_katalog dipisah karena juga dipakai ulang oleh order. 

## 8. Function Top Up Saldo<br>
<img width="1112" height="1064" alt="image" src="https://github.com/user-attachments/assets/ff71fe9e-30da-4883-ad7c-531d71d5d3e0" /><br>
<br<img width="1292" height="410" alt="image" src="https://github.com/user-attachments/assets/f5d8eeef-d6c7-45ec-be53-7febeb442771" /><br>
Fungsi ini menambah saldo pelanggan lewat paket top-up. program menampilkan daftar paket dari topup.json<br> 

## 9. Function Order Laundry<br>
<img width="2362" height="1324" alt="image" src="https://github.com/user-attachments/assets/46c007fc-ae59-407f-b851-4948e7dbfc6a" /><br>
<img width="2152" height="1370" alt="image" src="https://github.com/user-attachments/assets/be91e153-5090-44a8-b017-9d09242643eb" /><br>
<img width="1246" height="634" alt="image" src="https://github.com/user-attachments/assets/a334f1c6-c459-43f2-a4c6-bdfd91738d13" /><br>
Fngsi ini memproses pemesanan laundry dan alurnya cukup panjang. Pertama, program menampilkan katalog dan meminta ID layanan, lalu memvalidasinya. Jika kategori layanan "kiloan", pelanggan mengisi berat (Kg) dalam bentuk desimal, selain itu mengisi jumlah (pcs). Total dihitung dari harga dikali dengan jumlah, lalu program mengecek apakah saldo cukup. Jika cukup, program menampilkan ringkasan dan meminta konfirmasi ya/tidak. Setelah dikonfirmasi, saldo dipotong dan disimpan, ID transaksi acak "TRX-XXX" dibuat. Data transaksi dengan status "lunas" serta tanggal otomatis disimpan ke transaksi.json. Terakhir, fungsi cetak_invoice menampilkan struk.<br>

## 11. Function Cetak Invoice<br>
<img width="1068" height="586" alt="image" src="https://github.com/user-attachments/assets/84290f01-6e47-49ba-9a06-7873fe27f6fe" /><br>
Fungsi ini menampilkan struk setelah pelanggan berhasil melakukan order. Fungsi menerima dua data, yaitu data transaksi yang baru dibuat dan sisa saldo pelanggan. Program menampilkan judul "INVOICE LAUNDRY" lalu mencetak struk berisi nama pelanggan, ID transaksi, tanggal layanan, jumlah beserta satuannya (kg atau pcs), total harga dan status pembayaran, dan sisa saldo. Tampilan dipisahkan dengan pembayaran, dan sisa saldo. Pelanggan dapat menunggu pelanggan menekan enter untuk kembali.<br>

## 10. Function Riwayat Transaksi<br>
<img width="1206" height="1110" alt="image" src="https://github.com/user-attachments/assets/ba3b6e13-e145-4abf-8eff-536399a0a33b" /><br>
Fungsi ini Menampilkan semua transaksi milik pelanggan yang sedang login. program embaca file transksi.json dan menyaring hanya transaksi dengan username yang sama. Jika kosong, munvul "belum ada transaksi". Tetapi jika ada program akan mencetak struk dari setiap transaksi dan total pengeluaran.<br> 

## 11. Menu Admin<br>
<img width="712" height="567" alt="menu admin" src="https://github.com/user-attachments/assets/517eddd5-6556-431f-8a22-a03a34f77452" /><br>
Program menu admin dapat dijalankan ketika pengguna berhasil login sebagai admin. Program menampilkan daftar menu yang terdiri dari Manajemen layanan, Manajemen pelanggan, Manajaemen Top Up, Laporan keuangan, dan Kembali. Admin diminta memilih opsi dari 1 hingga 5 dalam perulangan while True, sehingga menu akan terus tampil hingga admin memilih untuk kembali. Setiap angka memiliki fungsi masing-masing: pilihan 1 membuka Manajemen Layanan, pilihan 2 Manajemen Pelanggan, pilihan 3 Manajemen Top Up, pilihan 4 Laporan keuangan, dan pilihan 5 mengembalikan admin ke menu utama melalui fungsi menu_utama(). Jika admin memasukkan pilihan di luar rentang tersebut, program menampilkan pesan kesalahan dan meminta input ulang.<br>

## 12. Manajemen Layanan<br>
<img width="731" height="717" alt="Manajemen layanan" src="https://github.com/user-attachments/assets/6f79fadc-0120-431f-b0a3-46ea90a20021" /><br>
Program ini dapat dijalankan jika pengguna memilih opsi 1. Fungsi manajemen_layanan() menampilkan menu utama pengelolaan layanan yang berisi pilihan untuk melihat, menambah, mengedit, menghapus, dan kembali ke menu admin. Semua data produk disimpan dalam file layanan.json yang digunakan oleh setiap fungsi terkait. Setelah menampilkan menu, program meminta admin memilih opsi dari 1 hingga 5. Pilihan 1 menampilkan daftar layanan melalui fungsi lihat_daftar(), pilihan 2 menambahkan layanan baru dengan tambah_layanan(), pilihan 3 mengedit data layanan melalui edit_layanan(), dan pilihan 4 menghapus layanan menggunakan hapus_layanan(). Jika admin memilih opsi 5, program akan memanggil fungsi admin() untuk kembali ke menu sebelumnya dan menghentikan perulangan.Jika admin memasukkan angka selain 1 sampai 5, program akan menampilkan pesan “Pilihan tidak valid, Silakan coba lagi”, dan meminta admin untuk memasukkan pilihan ulang yang benar.<br>

## 13. Fungsi lihat_daftar<br>
<img width="727" height="597" alt="Lihat daftar layanan" src="https://github.com/user-attachments/assets/c12fa4f4-26ae-40a9-9fc2-0c5eb68c80a3" /><br>
Fungsi lihat_daftar() menggunakan blok try-except untuk membaca data dari file JSON yang diberikan ke dalam list kosong jika terjadi kesalahan, lalu memeriksa ketersediaan data untuk menampilkan pesan "Layanan Belum Tersedia" jika kosong atau menyusun serta mencetak data tersebut ke dalam bentuk tabel berformat PrettyTable dengan kolom id, nama, harga, estimasi, dan kategori sebelum meminta input untuk melanjutkan.<br>




















































