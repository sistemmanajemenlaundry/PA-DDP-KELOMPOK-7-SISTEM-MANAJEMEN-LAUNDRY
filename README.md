

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
| **Shafa Aurellia Rufina Maharani** | `2609116001` | Program halaman admin & cek halaman program | @shafarufina8 (https://github.com/shafarufina8) |
| **Nazwa Dwi Amelia Putri** | `2609116008` | Laporan Bab 2 dan Bab 3 | @ameapples (https://github.com/ameapples) |
| **Deboraa Lintang Apsari** | `2609116011` | Flowchart dan referensi konsep program | @deboralintangapsari (https://github.com/deboralintangapsari) 
| **Raihanum Athaya Rana Insyra** | `2609116014` | Laporan Bab 1, halaman utama & halaman user | @raihanumathaya(https://github.com/raihanumathaya) |

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

Sistem akan membaca seluruh data dari file json dan program akan menampilkan layanan yang ada.<br
                                                                                                
`Proses Create` <br>

Pengguna akan memasukkan data baru, lalu program akan memvalidasi, jika tidak valid maka program akan menampilkan "Input Tidak Valid", dan meminta untuk memasukkan data baru, jika valid maka prograJika valid maka sistem akan mengecek apakah data/username sudah terdaftar di file JSON. Jika sudah ada maka program akan menampilkan "Data sudah terdaftar". Jika belum, data akan disimpan dan muncul esan "Data berhasil ditambah". 

`Proses Update (U)` 
Pengguna akan memasukkan ID/username yang ingin diubah. Jika data ditemukan, muncul pesan "Data tidak ditemukan". Apabila input valid, maka perubahan akan disimpan kedalam file json dan muncul pesan "Data berhasil diubah"

`Proses Delete (D)`

Penggua akan memasukkan ID/Username yang ingin dihapus. Jika data ditemukan, sistem menaampilkan rincian data dan meminta konfirmasi hapus (y/n). Jika dijawab Ya, data akan dihapus dari file json dan muncul pesan "data berhasil dihapus". Jika tidak, proses dibatalkan. 

`Laporan Pendapatan (LP)`

Pengguna akan memilih jenis laporan (1. Harian, 2. Bulanan, atau 3. Total).
Sistem akan membaca transaksi, menyaring sesuai pilihan dan menjumlahkan totalnya, lalu menampilkan rincian jumlah transaksi dan total pendapatan ke layar


4. Menu User <br>
<img width="1600" height="1392" alt="image" src="https://github.com/user-attachments/assets/73f91480-c4c9-4203-86ba-a3eeca18cb11" /> <br>

Program akan menampilkan menu user yaitu Katalog layanan, Saldo Top Up, Order Laundry, Riwayat Transaksi, Logout <br>

`Katalog Layanan` <br>
program akan membaca file dari json, mengecek apakah sudah ada layanan atau belum, jika tidak ada maka program akan menampilan "Belum ada layanan" dan jika sudah ada layanan maka Program akan menampilkan katalog layanan, user harus menekan tombol enter untuk kembali ke menu utama <br>

`Top Up Saldo` <br>
program akan membaca file dari json dan menampilkan saldo saat ini, program juga akan menampilkan paket top up, program akan mengecek apakah paket tersebut ada atau tidak, jika ada maka saldo akan ditambahkan ke akun user sesuai dengan nominal pada paket tersebut, perubahan akan disimpan kedalam folder json dan program akan menampilkan "Top Up berhasil" dan kembali ke menu utama. <br>

`Order Laundry` <br>
Program akan membaca file dari json, program akan mengecek apakah layanan tersedia, jika tidak makan program akan menampilkan "Belum ada layanan" dan jika terdapat layanan maka program akan menampilkan katalog layanan dan meminta user untuk memasukkan ID layanan, setelah itu program akan mengecek kembali apakah ID layanan nya ada, jika tidak ada maka program akan menampilkan "id layanan tidak ditemukan" dan akan kembali ke menu user, jika layanan ditemukan maka program akan bertanya apakah kategorinya kiloan, jika tidak berarti oderannya berupa satuan atau pcs, lalu program akan mengecek apakah input berupa angka lebih dari 0?, jika tidak maka program akan menampilkan "Input tidak valid", jika lebih dari 0 maka akan menghitung totalnya berdasarkan harga x jumlah, lalu program akan membaca data dari json, program akan melihat apakah saldo user cukup atau tidak, jika tidak maka program akan menampilkan "Saldo tidak mencukupi, silahkan top up!", jika saldo cukup maka program akan mengurangi saldo user sebesar total, lalu akan disimpan di file json dan program akan menampilkan "order berhasil". Dilakukan hal yang sama juga apabila ordernya kiloan. <br>

`Riwayat Transaksi` <br> 
Program akan membaca file dari json, lalu program akan mengambil transaksi dari user yang login, program akan mengecek apakah ada transaksi? jika tidak ada maka program akan menampilkan "Belum ada transaksi, balik ke menu", jika ada transaksi maka akan menampilkan riwayat transaksi dan menghitung total keseluruhan. <br>

`Logout` <br>
Program akan diakhiri dan kembali ke menu utama.

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
Fungsi ini memberi pengguna 3 kesempatan untuk login. Program meminta username dan password yang disembunyikan menggunakan pwinput yang kemudian dicocokan dengan data di users.json. jika cocok, program menampilkan pesan selamat datang dan mengarahkan sesuai roleh: admin ke admin() dan user ke menu_user(). Jika salah, kesempatan berkurang satu dan tersisa akan ditampilkan sampai habis.<br>

## 5. Function Registrasi <br>

<img width="1036" height="1226" alt="image" src="https://github.com/user-attachments/assets/579b5fe0-0157-412c-a434-acd80c005133" />
<img width="700" height="480" alt="image" src="https://github.com/user-attachments/assets/da8d67c4-0436-4f29-88fa-81cc6b542cda" /><br>
Fungsi ini membuat akun pelanggan baru. program memvalidasi bahwa username tidak kosong dan belum dipakai, password 4-8 karakter, serta nomor telepon berupa angka 10-13 digit. Jika semua valid, data baru ditambahkan dengan role user dan saldo awal 0, lalu disimpan ke users.json dengan save_users.

## 6. Function Menu User <br>
<img width="1326" height="1150" alt="image" src="https://github.com/user-attachments/assets/35a7f3b1-e23a-41e5-9a25-03b6b71f9747" /><br> 

Fungsi ini adalah menu utama setelah akun dengan role pelanggan berhasil login. Setiap kali menu tampil, program membaca ulang saldo terbaru dari users.json dan menampilkannya di bagian atas, menu memiliki 5 pilihan yaitu katalog Layanan, Top-Up Saldo, Order Laundry, Riwayat Transaksi, dan Logout. Pilihan 1-4 memanggil fungsi masing-masing dan kembali ke menu utama.<br>

## 7. Function Katalog Layanan<br>
<img width="1538" height="568" alt="image" src="https://github.com/user-attachments/assets/3f5fa965-13f5-4ce2-9dd1-a2ab16b303d3" /><br>

Fungsi tampilan_katalog dan katalog_layanan adalah untuk menampilkan daftar layanan dalam bentuk tabel PrettyTable dengan kolom ID, Nama, Kategori, Harga (berformat Rp), dan estimasi. Fungsi katalog membaca layanan.json, lalu memeanggil tampilan katalog jika data ada, atau menampilkan "Belum ada layanan" jika kosong. Fungsi tampilan_katalog dipisah karena juga dipakai ulang oleh order. 

## 8. Function Top Up Saldo<br>
<img width="1112" height="1064" alt="image" src="https://github.com/user-attachments/assets/ff71fe9e-30da-4883-ad7c-531d71d5d3e0" /><br>
<img width="1292" height="410" alt="image" src="https://github.com/user-attachments/assets/f5d8eeef-d6c7-45ec-be53-7febeb442771" /><br>

Fungsi ini menambah saldo pelanggan lewat paket top-up. program menampilkan daftar paket dari topup.json beserta saldo saat ini, lalu meminta kode paket. Jika kode ditemukan, saldo user ditambah sesuai nominal paket dan disimpan ke users.json. Setelah itu, riwayat top-up dicatat ke datatopup.json dan saldo terbaru ditampilkan.<br> 

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

## 13. Fungsi Lihat Daftar Layanan<br>
<img width="727" height="597" alt="Lihat daftar layanan" src="https://github.com/user-attachments/assets/c12fa4f4-26ae-40a9-9fc2-0c5eb68c80a3" /><br>

Fungsi lihat_daftar() menggunakan blok try-except untuk membaca data dari file JSON yang diberikan ke dalam list kosong jika terjadi kesalahan, lalu memeriksa ketersediaan data untuk menampilkan pesan "Layanan Belum Tersedia" jika kosong atau menyusun serta mencetak data tersebut ke dalam bentuk tabel berformat PrettyTable dengan kolom id, nama, harga, estimasi, dan kategori sebelum meminta input untuk melanjutkan.<br>

## 14. Fungsi Tambah Layanan<br>
<img width="922" height="822" alt="Tambah layanan" src="https://github.com/user-attachments/assets/41475435-e829-4022-bff4-b08b84c220f3" /><br>

Fungsi tambah_layanan() menampilkan header "TAMBAH LAYANAN", membaca data yang ada dari file JSON atau menginisialisasikannya sebagai list kosong jika terjadi kesalahan, lalu meminta input dari pengguna berupa ID dan nama layanan. Selanjutnya, program menggunakan perulangan while True dengan validasi try-except dan pengecekan angka negatif untuk memastikan harga serta estimasi diisi dengan angka valid yang tidak kurang dari nol, serta meminta input kategori. Program kemudian memeriksa apakah ID atau nama layanan tersebut sudah ada di dalam data secara case-insensitive untuk mencegah duplikasi, dan jika belum ada, data baru akan ditambahkan ke dalam list, disimpan kembali ke file JSON dengan format yang rapi menggunakan json.dump(), menampilkan pesan keberhasilan, serta memanggil fungsi lihat_daftar().<br>

## 15. Fungsi Edit Layanan<br>
<img width="787" height="851" alt="Edit layanan" src="https://github.com/user-attachments/assets/d2aeaf91-1701-4648-a305-86407c381341" /><br>
<img width="1257" height="432" alt="Edit layanan (2)" src="https://github.com/user-attachments/assets/e515e42f-761b-42b9-9deb-32171bb07582" /><br>

Fungsi edit_layanan() menangani proses pengubahan data layanan dengan terlebih dahulu membaca dan menampilkan daftar layanan yang ada dari file JSON, lalu meminta admin memasukkan ID layanan yang ingin diubah. Jika data ditemukan, program menampilkan detail lama dan memungkinkan admin memasukkan data baru untuk nama, harga, estimasi, dan kategori—di mana jika input dikosongkan maka data lama akan tetap dipertahankan, dilengkapi validasi perulangan while untuk memastikan harga serta estimasi bernilai angka valid dan tidak negatif. Setelah itu, program memperbarui data di dalam memori, menyimpan kembali perubahannya ke file JSON menggunakan json.dump(), menampilkan pesan keberhasilan, serta memanggil fungsi lihat_daftar(), atau menampilkan pesan kesalahan jika ID layanan tidak ditemukan.<br>

## 16. Fungsi Hapus Layanan<br>
<img width="1017" height="696" alt="Hapus layanan" src="https://github.com/user-attachments/assets/d6b13fca-d63e-4487-9ed1-ada306b7935b" /><br>

Fungsi hapus_layanan() menampilkan header "HAPUS LAYANAN", membaca data dari file JSON atau menginisialisasikannya sebagai list kosong jika terjadi kesalahan, lalu memanggil fungsi lihat_daftar() dan meminta admin memasukkan ID produk yang ingin dihapus. Program kemudian melakukan perulangan untuk mencari item dengan ID yang sesuai, menghapusnya dari list jika ditemukan, lalu meminta konfirmasi penghapusan ("ya/tidak") kepada pengguna. Jika pengguna mengetik "tidak", program akan membatalkan penghapusan dan keluar, sedangkan jika dikonfirmasi, program akan menyimpan kembali data yang telah diperbarui ke file JSON menggunakan json.dump(), menampilkan pesan keberhasilan, serta memanggil fungsi lihat_daftar(), atau menampilkan pesan bahwa produk dengan ID tersebut tidak ditemukan jika tidak ada yang cocok.<br>

## 17. Manajemen Pelanggan<br>
<img width="1141" height="740" alt="Manajemen pelanggan" src="https://github.com/user-attachments/assets/9242fbd3-a4f5-4109-8067-d85cbcedb382" /><br>

Fungsi manajemen_pelanggan() mengelola menu utama pengelolaan pelanggan yang menyimpan seluruh data pengguna pada file users.json, dengan menyediakan opsi 1 hingga 4 bagi admin untuk melihat daftar pelanggan melalui fungsi lihat_pelanggan(), menambah pelanggan baru dengan tambah_pelanggan(), mengubah data pelanggan melalui edit_pelanggan(), atau kembali ke menu sebelumnya dengan memanggil fungsi admin() yang menghentikan perulangan, serta menampilkan pesan peringatan jika input pilihan tidak valid.<br>

## 18. Fungsi Lihat Pelanggan<br>
<img width="1157" height="745" alt="Lihat pelanggan" src="https://github.com/user-attachments/assets/b98599b1-67b1-49ce-82f5-e8575a7195aa" /><br>

Fungsi lihat_pelanggan() menampilkan header "LIHAT PELANGGAN", membaca data dari file JSON pengguna atau menginisialisasikannya sebagai list kosong jika terjadi kesalahan, lalu menyaring data untuk hanya menampilkan akun yang bukan ber-role "admin". Jika data pelanggan kosong setelah disaring, program menampilkan pesan "Belum ada nama pelanggan yang terdaftar.", sedangkan jika ada, program menyusun dan mencetak datanya ke dalam bentuk tabel berformat PrettyTable dengan kolom username, no_telp, dan saldo sebelum meminta input dari pengguna untuk melanjutkan.<br>

## 19. Fungsi Tambah Pelanggan<br>
<img width="946" height="852" alt="tambah pelanggan" src="https://github.com/user-attachments/assets/5a0aa515-17e1-4f6e-91b6-a12555fdc059" /><br>

Fungsi tambah_pelanggan() menampilkan header "TAMBAH PELANGGAN", membaca data dari file JSON pengguna atau menginisialisasikannya sebagai list kosong jika terjadi kesalahan, lalu meminta input username dari admin dan memastikan username tersebut tidak kosong. Selanjutnya, program menggunakan perulangan while True bersama pustaka pwinput untuk meminta password dengan panjang antara 4 hingga 8 karakter serta meminta nomor telepon. Program memeriksa apakah username sudah terdaftar untuk mencegah duplikasi, dan jika belum ada, data baru dengan role "user" dan saldo awal 0 akan ditambahkan ke dalam list, disimpan kembali ke file JSON menggunakan json.dump(), menampilkan pesan keberhasilan, serta memanggil fungsi lihat_pelanggan().<br>

## 20. Fungsi edit pelanggan<br>
<img width="1077" height="846" alt="edit pelanggan" src="https://github.com/user-attachments/assets/6433d9b0-ac2e-419e-98a3-ef575f8e3960" /><br>

Fungsi edit_pelanggan() menampilkan header "EDIT PELANGGAN", membaca data dari file JSON pengguna, dan menangani error dengan menampilkan pesan jika file tidak ditemukan. Program kemudian meminta admin memasukkan username yang ingin diubah, mencari data pelanggan yang sesuai menggunakan fungsi next(), serta menampilkan pesan kesalahan jika username tidak ditemukan. Jika data ditemukan, program mencetak detail data lama—dengan menyembunyikan password menjadi bintang-bintang (*****) lalu meminta input nomor telepon baru di mana jika dikosongkan (menekan Enter), nomor telepon lama akan tetap dipertahankan. Terakhir, program menyimpan perubahan tersebut kembali ke file JSON menggunakan json.dump(), menampilkan pesan keberhasilan, dan menjeda eksekusi selama 2 detik.<br>

## 21. Fungsi Hapus Pelanggan<br>
<img width="1185" height="850" alt="hapus pelanggan" src="https://github.com/user-attachments/assets/ae10ebc6-2086-4c86-820a-948be80340de" /><br>

Fungsi hapus_pelanggan() menampilkan header "HAPUS PELANGGAN", membaca data dari file JSON pengguna atau menginisialisasikannya sebagai list kosong jika terjadi kesalahan, lalu menyaring data untuk mengambil akun yang bukan ber-role "admin". Jika data pelanggan kosong, program menampilkan pesan "Belum ada data pelanggan yang terdaftar." dan menghentikan proses, sedangkan jika ada, program memanggil fungsi lihat_pelanggan() dan meminta admin memasukkan username pelanggan yang ingin dihapus. Program mencari data berdasarkan username tersebut, dan jika tidak ditemukan, program menampilkan pesan kesalahan serta menjeda eksekusi selama 1 detik sebelum keluar. Jika ditemukan, program menampilkan detail data yang akan dihapus, meminta konfirmasi penghapusan ("ya/tidak"), membatalkan proses jika jawabannya bukan "ya", dan jika dikonfirmasi, data pelanggan akan dihapus dari list serta disimpan kembali ke file JSON menggunakan json.dump() disertai penanganan error try-except untuk memastikan perubahan berhasil tersimpan.<br>

## 22. Manajemen Top Up<br>
<img width="1392" height="586" alt="Manajemen top up" src="https://github.com/user-attachments/assets/c7e60050-acb4-406a-b122-a2431e1ea8b0" /><br>

Fungsi manajemen_topup() mengelola menu utama pengelolaan paket top-up yang membaca data dari file topup.json menggunakan fungsi load_json(), lalu menyusun dan menampilkan daftar paket tersebut dalam bentuk tabel berformat PrettyTable dengan kolom Kode, Nama Paket, dan Nomor Nominal (atau menampilkan pesan "Belum ada paket top-up yang tersedia." jika data kosong). Setelah itu, program menampilkan menu pilihan pengelolaan yang mencakup opsi 1 untuk menambah paket baru, opsi 2 untuk menghapus paket, opsi 3 untuk melihat riwayat pelanggan yang top-up, serta opsi 4 untuk kembali ke menu admin, dan meminta input pilihan dari pengguna.<br>

##23. Tambah Paket Top Up Baru<br>
<img width="1142" height="642" alt="tambah paket" src="https://github.com/user-attachments/assets/ae5d8d13-7a9f-49c8-ad3f-37d343f7da7f" /><br>

Blok kode di atas menangani pilihan 1 untuk menambahkan paket top-up baru dengan mencetak header, meminta input kode (yang otomatis diubah menjadi huruf kapital dan dipangkas spasi) dengan validasi agar tidak kosong. Program kemudian meminta input nama paket serta nominal saldo—dilengkapi validasi menggunakan blok try-except dan pengecekan angka negatif untuk memastikan nominal berupa angka valid dan tidak kurang dari nol. Jika semua data valid, paket baru tersebut ditambahkan ke dalam list data_paket, disimpan kembali ke file JSON menggunakan fungsi save_json(), menampilkan pesan keberhasilan, dan menjeda eksekusi selama 2 detik sebelum melanjutkan perulangan.<br>

##24. Hapus Paket Top Up<br>
<img width="1337" height="597" alt="hapus paket" src="https://github.com/user-attachments/assets/c33b25d7-7521-44a5-8132-24e443d37af1" /><br>

Bagian kode di atas menangani pilihan 2 untuk menghapus paket top-up dengan terlebih dahulu memeriksa apakah `data_paket` kosong, dan jika kosong akan menampilkan pesan "Tidak ada paket untuk dihapus." lalu menjeda eksekusi selama 2 detik sebelum melanjutkan perulangan. Jika ada data, program meminta admin memasukkan kode paket yang ingin dihapus (yang otomatis dipangkas spasi dan diubah menjadi huruf kapital). Program kemudian melakukan perulangan untuk mencari paket dengan kode yang sesuai, menghapusnya dari list data_paket, mengubah status found menjadi True, dan menghentikan pencarian (break). Terakhir, jika paket ditemukan, program menyimpan perubahan ke file JSON menggunakan fungsi save_json() dan menampilkan pesan "Paket top-up berhasil dihapus!", sedangkan jika tidak ditemukan, program menampilkan pesan "Kode paket tidak ditemukan!" disertai jeda 2 detik.<br>

## 25. Lihat riwayat pelanggan yang top up<br>
<img width="1445" height="782" alt="riwayat" src="https://github.com/user-attachments/assets/55d5371c-04a8-478f-a6cb-6c0e96645482" /><br>

Jika admin memilih opsi 3, program menampilkan header "RIWAYAT TOP-UP PELANGGAN", membaca data riwayat dari file datatopup.json menggunakan fungsi load_json(), dan memeriksa ketersediaannya—di mana jika kosong, program mencetak pesan "Belum ada pelanggan yang melakukan top-up." Jika data tersedia, program menyusun tabel berformat PrettyTable dengan kolom Username, Kode Paket, Nomor, dan Tanggal, melakukan perulangan untuk memasukkan data setiap riwayat, serta menghitung akumulasi total dana top-up masuk (total_dana). Setelah tabel dan total keseluruhan dana dicetak, program menghentikan sementara eksekusi menggunakan input("Tekan Enter untuk kembali..."). Sementara itu, jika admin memilih opsi 4, program akan menjalankan perintah break untuk menghentikan perulangan menu dan kembali ke menu sebelumnya. Jika admin memasukkan pilihan selain opsi yang tersedia, blok else akan mencetak pesan "Pilihan tidak valid!" dan menjeda eksekusi selama 1 detik.<br>

## 26. Laporan Keuangan<br>
<img width="1291" height="776" alt="laporan keuangan" src="https://github.com/user-attachments/assets/3a6f32a7-b275-402f-b76f-bbff3dfe467f" /><br>

Fungsi laporan_keuangan() menampilkan header "LAPORAN KEUANGAN USAHA LAUNDRY", lalu memuat data transaksi dari file transaksi.json dan menjumlahkan total pendapatan laundry melalui perulangan for. Selanjutnya, fungsi membaca data dari file datatopup.json untuk menghitung total pemasukan dari saldo top-up, lalu menggabungkan keduanya ke dalam variabel pendapatan_total. Program kemudian mencetak rincian laporan yang mencakup total pendapatan laundry, total pemasukan top-up, total keseluruhan keuangan masuk (dengan format angka ribuan yang rapi), serta jumlah total transaksi laundry dan aktivitas top-up, sebelum menghentikan sementara eksekusi menggunakan input("Tekan Enter untuk kembali ke Menu Admin...").<br>








# Output dan Alur Penggunaannya
##  1. Menu Utama<br>
Tampilan awal program dengan tiga pilihan yaitu login, registrasi, dan keluar. Pengguna memiliki salah satunya dengan mengetik angka 1 sampai 3.<br>

<img width="468" height="201" alt="image" src="https://github.com/user-attachments/assets/ab8e3edf-57b0-4033-9866-60839ce81412" /><br>

##  2. Login<br>
Pengguna memasukkan username dan password. Password tampil sebagai tanda `*` agar tidak terlihat. Jika cocok, muncul pesan “Login berhasil! Selamat datang, (user)” dan program akan langsung membuka menu user.<br>

<img width="468" height="353" alt="image" src="https://github.com/user-attachments/assets/d7e7b3cd-612b-4c1b-90c0-b7b0854d6a03" />
<br>

## 3. Menu User<br>
Menu untuk pelanggan setelah login akan ditampilkan. Pada bagian atas menampilkan nama pengguna dan saldo terbaru. Pilihan untuk menu user mencakup Katalog Layanan, Top Up Saldo, Order Laundry, Riwayat Transaksi, dan Logout.<br>

￼<img width="468" height="218" alt="image" src="https://github.com/user-attachments/assets/29814482-cd36-45b9-9096-9edaa0d8ec14" />

<br>

## 4. Menu User - Katalog Layanan<br>
Setelah memilih menu 1, daftar layanan ditampilkan dalam tabel berisi ID, nama, kategori, harga, dan estimasi pengerjaan. Tekan enter untuk kembali ke Menu User.<br>

<img width="468" height="374" alt="image" src="https://github.com/user-attachments/assets/8ebcc1db-f92a-4f83-9944-88b181dc568c" /><br>

##  5. Menu User - Top Up Saldo<br>
Setelah memilih menu 2, program menampilkan paket top-up dengan kode yang dimulai dari L001-L003) beeserta saldo yang ada saat ini. Pelanggan memasukkan kode paket, lalu saldo bertambah sesuai nominalnya.<br>

<img width="468" height="336" alt="image" src="https://github.com/user-attachments/assets/2dabb23a-e3fc-4d86-b86e-2cc8a6da8a6b" /><br>

## 6.  Menu User - Order Laundry dan Invoice<br>
Setelh user memilih menu 3. Pelanggan memilih ID layanan (L001) dan memasukkan berat 3kg. Programmenghitung total biaya dan menampilkan sisa saldo lalu meminta konfirmasi pembayaran. Setelah dikonfirmasi, saldo terpotong otomatis dan invoice dicetak berisi ID transaksi, tanggal, layanan, jumlah, dan total harga.<br>

￼<img width="468" height="642" alt="image" src="https://github.com/user-attachments/assets/dd9f3e94-b533-4e7c-9741-39d67d7af2a8" /><br>

## 7. Menu user - Riwayat Transaksi<br>
Di dalam menu 4, program menampilkan semua transaksi milik pelanggan yang sedang login, lengkap dengan ID, tanggal, layanan, jumlah, status, dan total harga. Di bagian bawah ada total keseluruhan pengeluaran.<br>

<img width="468" height="584" alt="image" src="https://github.com/user-attachments/assets/f4ee57ef-6692-42d1-a0d7-a9bd26528747" /><br>

## 8. Menu User - Logout <br>
Memilih menu 5 di menu user akan mengakhir sesi pelanggan. Saldo terakhir sudah sesuai dengan semua transaksi dan akhirnya kembali ke menu utama.<br>

<img width="468" height="367" alt="image" src="https://github.com/user-attachments/assets/972bbc32-57a9-4d37-93f1-383647988376" /><br>


## 9. Menu User - Registrasi<br>
Muncul setelah memilih menu 2 di menu utama. pengguna mengisi username baru, password (4-8 karakter) dan nomor telepon (10-13 digit angka). Jika semua valid, muncul pesan akun berhasil ditambahkan!” dan program kembali ke Menu utama<br>

<img width="468" height="420" alt="image" src="https://github.com/user-attachments/assets/672c266d-833f-4a73-a8bc-b50478426a10" /><br>

## 10. Menu Utama Laundry<br>
Tangkapan layar ini menampilkan proses awal masuk ke dalam sistem melalui Menu Utama Laundry dengan memilih opsi login, memasukkan kredensial admin (username dan password), hingga berhasil masuk dan diarahkan ke halaman Menu Admin utama.<br>

<img width="610" height="523" alt="image" src="https://github.com/user-attachments/assets/a3e761b1-7ce9-463e-979b-0ce25598f430" /><br>

## 11. Lihat Daftar Layanan<br>
Tangkapan layar ini menunjukkan menu Manajemen Layanan saat admin memilih opsi untuk melihat daftar layanan, di mana sistem menampilkan tabel berisi informasi lengkap mengenai ID, nama, harga, estimasi waktu, dan kategori dari setiap layanan laundry yang tersedia.<br>

<img width="622" height="600" alt="image" src="https://github.com/user-attachments/assets/39ef7a99-f1b4-47dd-b8ea-f142563dd1f0" /><br>

## 12. Tambah Layanan Baru<br>
Tangkapan layar ini memperlihatkan proses penambahan layanan laundry baru ke dalam sistem dengan memasukkan data seperti ID, nama, harga, estimasi, dan kategori, yang kemudian langsung memperbarui dan menampilkan daftar layanan terbaru.<br>

<img width="616" height="617" alt="image" src="https://github.com/user-attachments/assets/e84d2419-805f-4664-b2f7-e4386159a71c" /><br>

## 13. Edit Data layanan<br>
Tangkapan layar ini menampilkan proses pengubahan atau pengeditan data layanan yang sudah ada berdasarkan ID tertentu, di mana admin dapat memperbarui informasi nama, harga, estimasi, atau kategori layanan sesuai kebutuhan.<br>

<img width="435" height="572" alt="image" src="https://github.com/user-attachments/assets/672432d0-a479-4bcf-91ba-85165a49f155" /><br>

## 14. Hapus Layanan<br>
Tangkapan layar ini menunjukkan proses penghapusan suatu layanan dari sistem berdasarkan ID produk yang dipilih, yang disertai dengan konfirmasi keamanan sebelum data layanan tersebut berhasil dihapus dari daftar.<br>

<img width="438" height="459" alt="image" src="https://github.com/user-attachments/assets/3174a104-b76c-4b8c-b2c2-bc02da94b07f" /><br>

## 15. Kembali ke Menu Admin dari Manajemen Layanan<br>
Tangkapan layar ini memperlihatkan tindakan admin saat memilih opsi untuk keluar dari sub-menu Manajemen Layanan dan kembali ke halaman utama Menu Admin.<br>

<img width="492" height="290" alt="image" src="https://github.com/user-attachments/assets/1cd05411-1cae-4b08-93bb-e2a81550f922" /><br>

## 16. Manajemen Pelanggan (Lihat Daftar Pelanggan)<br>
Tangkapan layar ini menampilkan akses ke menu Manajemen Pelanggan untuk melihat daftar seluruh akun pelanggan terdaftar (di luar akun admin) beserta informasi username, nomor telepon, dan saldo mereka dalam bentuk tabel.<br>

<img width="975" height="704" alt="image" src="https://github.com/user-attachments/assets/c5e7f8d3-25e6-42f1-8376-85890ab35f77" /><br>

## 17. Tambah Pelanggan Baru<br>
Tangkapan layar ini memperlihatkan proses pendaftaran atau penambahan pelanggan baru ke dalam sistem oleh admin dengan memasukkan data username, password, dan nomor telepon.<br>

<img width="975" height="578" alt="image" src="https://github.com/user-attachments/assets/edfe4187-05b6-4fb3-b060-db4feb50364c" /><br>

## 18. Edit Data Pelanggan<br>
Tangkapan layar ini menunjukkan proses pembaruan informasi data pelanggan yang sudah terdaftar, khususnya dalam memperbarui nomor telepon pelanggan berdasarkan username yang dipilih.<br>

<img width="975" height="735" alt="image" src="https://github.com/user-attachments/assets/3bf867fb-cb68-4779-b14c-f3f660eb08a3" /><br>

## 19. Manajemen Top-Up (Tambah Paket Top-Up Baru)<br>
Tangkapan layar ini menampilkan pengelolaan paket top-up saldo, di mana admin dapat melihat daftar paket yang ada serta menambahkan paket top-up baru dengan memasukkan kode, nama paket, dan nominal saldonya.<br>

<img width="438" height="485" alt="image" src="https://github.com/user-attachments/assets/31a77cbb-5936-4005-b6a3-1d0c292c7747" /><br>

## 20. Hapus Paket Top-Up<br>
Tangkapan layar ini memperlihatkan proses penghapusan paket top-up tertentu dari sistem berdasarkan kode paket yang dimasukkan oleh admin.<br>

<img width="643" height="406" alt="image" src="https://github.com/user-attachments/assets/1959d2e1-f3d6-4013-89dc-e28a9d28b442" /><br>

## 21. Riwayat Top-Up Pelanggan<br>
Tangkapan layar ini menampilkan daftar riwayat transaksi top-up saldo yang pernah dilakukan oleh para pelanggan beserta total keseluruhan dana top-up yang masuk ke dalam sistem.<br>

<img width="591" height="658" alt="image" src="https://github.com/user-attachments/assets/e6948a9e-331f-417b-aaa4-2911ada9c309" /><br>

## 22. Laporan Keuangan Usaha Laundry<br>
Tangkapan layar ini menunjukkan halaman Laporan Keuangan yang merinci total pendapatan dari order laundry, total pemasukan dari top-up saldo, total keseluruhan keuangan masuk, serta jumlah total transaksi dan aktivitas top-up yang telah diselesaikan.<br>

<img width="526" height="367" alt="image" src="https://github.com/user-attachments/assets/b984dac6-901c-4f4a-849c-385c24045c8e" /><br>

## 23. Keluar / Kembali ke Menu Utama Laundry<br>
Tangkapan layar ini memperlihatkan saat admin memilih opsi keluar dari Menu Admin untuk kembali ke tampilan awal Menu Utama Laundry.<br>

<img width="597" height="374" alt="image" src="https://github.com/user-attachments/assets/6b7d6aaf-a0eb-4ee6-8067-e83cad0c566c" /><br>





                                                                                                                                                                                                                                          







































































