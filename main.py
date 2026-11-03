# ========================== LIBRARY YANG DIGUNAKAN ============================
import os
import json
import time
import random
import pwinput
from prettytable import PrettyTable
# ========================== FUNCTION PENDUKUNG ================================
def bersih(): 
    os.system("cls" if os.name == "nt" else "clear")

def header(judul): #fungsi untuk header
    bersih()
    print("\n"*2)
    print("="*70)
    print(f"|{judul.center(68).upper()}|")
    print("="*70)

def load_json(transaksi): 
    try:
        with open(transaksi, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {transaksi} tidak dapat ditemukan.")
        return []
    except json.JSONDecodeError:
        print(f"File {transaksi} rusak.")
        return []

def save_json(transaksi, data): 
    try:
        with open(transaksi, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Gagal menyimpan data:{e}")

def load_users(): 
    try: 
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File users.json tidak dapat ditemukan.")
        return menu_utama
    except json.JSONDecodeError:
        print("File users.json rusak.")
        return menu_utama
    
def save_users(data): 
    try:
        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Gagal menyimpan data{e}")

def cari_user(users, username): 
    for u in users:
        if u["username"] == username:
            return u
    return None

def lihat_daftar(json_file):

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if not data:
        print("\nLayanan Belum Tersedia")
        return data
    tabel = PrettyTable()
    tabel.field_names = ["id","nama","harga","estimasi", "kategori"]
    for item in data:
        tabel.add_row([
            item.get("id", "-"),
            item.get("nama", "-"),
            item.get("harga", "-"),
            item.get("estimasi", "-"),
            item.get("kategori", "-")
        ])
    print(tabel)
    input("\nTekan Enter untuk lanjut...")
    return data

def tambah_layanan(json_file):
    header("TAMBAH LAYANAN")

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    id = input("Masukkan ID layanan: ")
    nama_layanan = input("Masukkan nama Layanan: ")

    while True:
        try:
            harga = int(input("Masukkan harga:"))
            if harga < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Masukkan angka yang benar!")

    while True:
        try:
            estimasi = int(input("Masukkan estimasi: "))
            if estimasi < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Masukkan angka yang benar!")

    kategori = input("Masukkan kategori: ")

    for item in data:
        if item.get("id") == id or item.get("nama", "").lower() == nama_layanan.lower():
            print("\nLayanan sudah ada!\n")
            return
    data.append({
        "id": id,
        "nama": nama_layanan,
        "harga": harga,
        "estimasi": estimasi,
        "kategori": kategori
    })

    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)
    print("\nLayanan baru berhasil ditambahkan!")
    lihat_daftar(json_file)

def edit_layanan(json_file):
    header("EDIT DATA LAYANAN")

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File Tidak Ditemukan!")
        time.sleep(1)
        return

    data = lihat_daftar(json_file)
    id = input("Masukkan ID layanan yang ingin di edit: ")
    found = False
    for item in data:
        if item.get("id") == id:
            found = True
            print("\nData lama: ")
            for kunci, nilai in item.items():
                print(f"-{kunci}: {nilai}")
            print("\nTekan ENTER jikan ingin lewati...")
            nama = input(f"Masukkan nama layanan [{item.get('nama')}]: ") or item.get("nama")

            while True:
                harga_input = input(f"masukkan harga [{item.get('harga')}]: ")
                if harga_input.strip() == "":
                    harga = item.get("harga")
                    break
                try:
                    harga = int(harga_input)
                    if harga < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang benar!")

            while True:
                estimasi = input(f"Masukkan estimasi [{item.get('estimasi')}]: ")
                if estimasi.strip() == "":
                    estimasi = item.get("estimasi")
                    break

                try:
                    estimasi= int(estimasi)
                    if estimasi < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang benar!")

            kategori = input(f"Masukkan kategori produk [{item.get('kategori')}]: ") or item.get("kategori")
            item.update({
                "nama": nama,
                "harga": harga,
                "estimasi": estimasi,
                "kategori": kategori
            })
            break

    if found:
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
        print("\nLayanan berhasil diedit")
        lihat_daftar(json_file)
    else:
        print("\nLayanan dengan ID tersebut tidak ditemukan!\n")
        time.sleep(1)


def hapus_layanan(json_file):
    header("HAPUS LAYANAN")

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data = lihat_daftar(json_file)
    id = input("Masukkan ID produk yang ingin di hapus: ")
    found = False
    for item in data:
        if item.get("id") == id:
            found = True
            data.remove(item)
    konfirmasi = input("Konfirmasi hapus (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Batal menghapus layanan")
        return
    
    elif found:
        with open(json_file,"w") as file:
            json.dump(data, file, indent=4)
        print("\nLayanan berhasil dihapus!\n")
        lihat_daftar(json_file)
    else:
        print("\nProduk dengan ID tersebut tidak ditemukan!\n")
        time.sleep(1)


def manajemen_layanan():
    header("MANAJEMEN LAYANAN")
    print("1. Lihat ")
    print("2. Tambah Layanan Baru")
    print("3. Edit data Layanan")
    print("4. Hapus Layanan")
    print("5. Kembali")

    json_file = "layanan.json"

    while True:
        pilihan_admin = input("Masukkan pilihan Anda: ")
        if pilihan_admin == "1":
            lihat_daftar(json_file)
            manajemen_layanan()
        elif pilihan_admin == "2":
            tambah_layanan(json_file)
            manajemen_layanan()
        elif pilihan_admin == "3":
            edit_layanan(json_file)
            manajemen_layanan()
        elif pilihan_admin == "4":
            hapus_layanan(json_file)
            manajemen_layanan()
        elif pilihan_admin == "5":
            admin()
            break
        else:
            print("Pilihan Tidak Valid! Silahkan coba lagi.")

def lihat_pelanggan(json_file2):
    header("LIHAT PELANGGAN")

    try:
        with open(json_file2, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        
    data = [item for item in data if item.get("role") != "admin"]

    if not data:
        print("\nBelum ada nama pelanggan yang terdaftar.\n")
        return data
    tabel = PrettyTable()
    tabel.field_names = ("username","no_telp", "saldo")
    for item in data:
        tabel.add_row([
            item.get("username", "-"),
            item.get("no_telp", "-"),
            item.get("saldo", "-")
        ])
    print(tabel)
    input("\nTekan Enter untuk lanjut...")
    return data

def tambah_pelanggan(json_file2):
    header("TAMBAH PELANGGAN")
    try:
        with open(json_file2, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 

    username = input("Masukkan Username Pelanggan: ")
    if not username:
        print("Username tidak boleh kosong!")
        return

    while True:
        password = pwinput.pwinput("Masukkan passworn (4-8 karakter):")
        if 4<= len(password) <= 8:
            break
        print("Password harus memiliki panjang antara 4-8 karakter")
        
    if not password:
        print("Password tidak boleh kosong")
        return
    
    no_telp = input("Masukkan nomor telepon: ")


    for item in data:
        if item.get("username", "") == username:
            print("\nPelanggan sudah ada!\n")
            return

    data.append ({
        "username": username,
        "password": password,
        "role": "user",
        "no_telp": no_telp,
        "saldo": 0
    })
    with open(json_file2, "w") as file:
        json.dump(data, file, indent=4)
    print("\nPelanggan baru sudah berhasil ditambahkan!")
    lihat_pelanggan(json_file2)

def edit_pelanggan(json_file2):
    header("EDIT PELANGGAN")

    try:
        with open(json_file2, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File tidak ditemukan!")
        time.sleep(1) 
        return

    username = input("Masukkan username yang ingin diubah: ")
    item = next((pelanggan for pelanggan in data
    if pelanggan.get("username") == username), None)
    if item is None:
        print("\nPelanggan dengan username tersebut tidak ditemukan!\n")
        time.sleep(1)
        return

    print("\nData lama: ")
    for kunci, nilai in item.items():
        if kunci == "password":
            print(f"{kunci}: *****")
        else:
            print(f"-{kunci}: {nilai}")
    print("Tekan ENTER jika ingin dilewati...")

    telepon_baru = input(f"Masukkan nomor no_telp [{item.get('no_telp', '-')}]:").strip()
    if telepon_baru:
        item["no_telp"] = telepon_baru

    with open(json_file2, 'w') as file:
        json.dump(data, file, indent=4)
    print("\nData pelanggan berhasil diubah!\n")
    time.sleep(2)

def hapus_pelanggan(json_file2):
    header("HAPUS PELANGGAN")
    try:
        with open(json_file2, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    pelanggan = [item for item in data if item.get("role") != "admin"]
    if not pelanggan:
        print("Belum ada data pelanggan yang terdaftar.")
        return

    lihat_pelanggan(json_file2)
    username_hapus = input("\nMasukkan Username Pelanggan yang ingin dihapus: ")

    pelanggan_dipilih = None
    for item in pelanggan:
        if item.get("username", "") == username_hapus:
            pelanggan_dipilih = item
            break

    if not pelanggan_dipilih:
        print("\nPelanggan dengan username tersebut tidak ditemukan!\n")
        time.sleep(1)
        return

    print(f"\nData yang akan dihapus >> username:{pelanggan_dipilih.get('username')} | Telp: {pelanggan_dipilih.get('no_telp', '-')}")
    konfirmasi = input("Konfirmasi hapus? (ya/tidak): ").strip().lower()

    if konfirmasi != "ya":
        print("Batal menghapus data pelanggan.")
        return

    data.remove(pelanggan_dipilih)

    try:
        with open(json_file2, "w") as file:
            json.dump(data, file, indent=4)
        print("\nPelanggan berhasil dihapus!\n")
    except Exception as e:
        print(f"\nGagal menyimpan perubahan: {e}\n")

def manajemen_pelanggan():
    header("MANAJEMEN PELANGGAN")
    print("1. Lihat Daftar Pelanggan")
    print("2. Tambah Pelanggan Baru")
    print("3. Edit Data Pelanggan")
    print("4. Kembali")
    

    json_file2 = "users.json"
    while True:
            pilihan_admin = input("Masukkan Pilihan Anda: ")
            if pilihan_admin == "1":
                lihat_pelanggan(json_file2)
                manajemen_pelanggan()
            elif pilihan_admin == "2":
                tambah_pelanggan(json_file2)
                manajemen_pelanggan()
            elif pilihan_admin == "3":
                edit_pelanggan(json_file2)
                manajemen_pelanggan()
            elif pilihan_admin == "4":
                admin()
                break
            else:
                print("Pilihan tidak valid! Silahkan coba lagi.")

# ========================== MANAJEMEN PAKET TOP-UP (ADMIN) ==================
def manajemen_topup():
    json_file = "topup.json"
    
    while True:
        header("MANAJEMEN PAKET TOP-UP")
        data_paket = load_json(json_file)

        tabel = PrettyTable()
        tabel.field_names = ["Kode", "Nama Paket", "Nominal"]
        if data_paket:
            for p in data_paket:
                tabel.add_row([p.get("kode", "-"), p.get("nama_paket", "-"), f"Rp{p.get('nominal', 0):,}"])
            print(tabel)
        else:
            print("Belum ada paket top-up yang tersedia.")
        
        print("\nMenu Kelola Paket:")
        print("1. Tambah Paket Top-Up Baru")
        print("2. Hapus Paket Top-Up")
        print("3. Lihat Riwayat Pelanggan yang Top-Up")
        print("4. Kembali ke Menu Admin")
        
        pilihan = input("Masukkan pilihan Anda: ").strip()
        
        if pilihan == "1":
            print("\n" + "="*40)
            print("         Tambah Paket Top-Up Baru")
            print("="*40)
            kode = input("Masukkan Kode (Cth: L004): ").strip().upper()
            if not kode:
                print("Kode tidak boleh kosong!")
                time.sleep(2)
                continue
                
            nama = input("Masukkan Nama Paket (Cth: Top Up Super): ").strip()
            try:
                nominal = int(input("Masukkan Nominal (Cth: 50000): ").strip())
                if nominal < 0:
                    print("Nominal tidak boleh negatif!")
                    time.sleep(2)
                    continue
            except ValueError:
                print("Nominal harus berupa angka yang valid!")
                time.sleep(2)
                continue
                
            data_paket.append({"kode": kode, "nama_paket": nama, "nominal": nominal})
            save_json(json_file, data_paket)
            print("\nPaket top-up berhasil ditambahkan!")
            time.sleep(2)
            
        elif pilihan == "2":
            if not data_paket:
                print("\nTidak ada paket untuk dihapus.")
                time.sleep(2)
                continue
                
            kode_hapus = input("\nMasukkan Kode paket yang ingin dihapus: ").strip().upper()
            found = False
            for p in data_paket:
                if p.get("kode") == kode_hapus:
                    data_paket.remove(p)
                    found = True
                    break
                    
            if found:
                save_json(json_file, data_paket)
                print("\nPaket top-up berhasil dihapus!")
            else:
                print("\nKode paket tidak ditemukan!")
                time.sleep(2)
            
        elif pilihan == "3":
            header("RIWAYAT TOP-UP PELANGGAN")
            data_riwayat = load_json("datatopup.json")
            if not data_riwayat:
                print("Belum ada pelanggan yang melakukan top-up.")
            else:
                tabel_riwayat = PrettyTable()
                tabel_riwayat.field_names = ["Username", "Kode Paket", "Nominal", "Tanggal"]
                total_dana = 0
                for r in data_riwayat:
                    nom = r.get("nominal", 0)
                    tabel_riwayat.add_row([
                        r.get("username", "-"),
                        r.get("kode_paket", "-"),
                        f"Rp{nom:,}",
                        r.get("tanggal", "-")
                    ])
                    total_dana += nom
                print(tabel_riwayat)
                print(f"\nTotal Keseluruhan Dana Top-up Masuk: Rp{total_dana:,}")
            input("\nTekan Enter untuk kembali...")
            
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)

def laporan_keuangan():
    header("LAPORAN KEUANGAN USAHA LAUNDRY")

    transaksi = load_json("transaksi.json")
    total_laundry = 0
    for t in transaksi:
        total_laundry += t.get("total", 0)
    
    topup_data = load_json("datatopup.json")
    total_topup = 0
    for tp in topup_data:
        total_topup += tp.get("nominal", 0)

    pendapatan_total = total_laundry + total_topup
    
    print("=" * 55)
    print(f"Total Pendapatan dari Order Laundry : Rp{total_laundry:,}")
    print(f"Total Pemasukan dari Top-Up Saldo   : Rp{total_topup:,}")
    print("-" * 55)
    print(f"TOTAL KESELURUHAN KEUANGAN MASUK     : Rp{pendapatan_total:,}")
    print("=" * 55)
    print(f"Jumlah Transaksi Laundry Selesai     : {len(transaksi)} transaksi")
    print(f"Jumlah Aktivitas Top-Up Saldo        : {len(topup_data)} aktivitas")
    print("=" * 55)
    
    input("\nTekan Enter untuk kembali ke Menu Admin...")

def admin():
    while True:
        header("MENU ADMIN")
        print("1. Manajemen Layanan")
        print("2. Manajemen Pelanggan")
        print("3. Manajemen Top Up")
        print("4. Laporan Keuangan")
        print("5. kembali")

        pilihan_admin = input("Masukkan pilihan Anda: ").strip()
        if pilihan_admin == "1":
            manajemen_layanan()
        elif pilihan_admin == "2":
            manajemen_pelanggan()
        elif pilihan_admin == "3":
            manajemen_topup()
        elif pilihan_admin == "4":
            laporan_keuangan()
        elif pilihan_admin == "5":
            menu_utama()
            return
        else:
            print("Pilihan Tidak Valid! Silahkan Coba Lagi")

def regis(): 
    data_users = load_users()
    bersih()
    print("\n"*2)
    header("REGISTRASI")
    username = input("Masukkan username baru: ").strip()
    
    if username == "":
        print("username tidak boleh kosong.")
        time.sleep(2)
        return
    for u in data_users:
        if u["username"] == username:
            print("username sudah digunakan.")
            time.sleep(2)
            return
    
    while True:
        password = pwinput.pwinput("Masukkan password: ").strip()
        if 4 <= len(password) <= 8:
            break
        print("Password harus memiliki 4-8 karakter.")
        
    if password == "":
        print("password tidak boleh kosong.")
        time.sleep(2)
        return
    
    no_telp = input("Daftarkan nomor telepon: ").strip()
    if not no_telp.isdigit() or not (10 <= len(no_telp) <= 13):
        print("Nomor telepon berupa angka. Wajib 10-13 digit.")
        time.sleep(2)
        return
    
    data_users.append(
        {
            "username": username,
            "password": password,
            "role": "user",
            "no_telp": no_telp,
            "saldo": 0
        }
    )
    save_users(data_users)
    print("Akun berhasil ditambahkan!")
    time.sleep(2)

def login(): 
    data_users = load_users()
    kesempatan = 3 
    while kesempatan > 0:
        bersih()
        print("\n"*2)
        print("="*70)
        print("|                             MENU LOGIN                             |")
        print("="*70)
        username = input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan Password: ").strip()
        
        found = None
        for u in data_users:
            if u["username"] == username and u["password"] == password:
                found = u
        if found:
            print(f"\nLogin berhasil! Selamat datang, {found['username']}")
            time.sleep(2)
            if found["role"] == "admin":
                admin()
            else: 
                menu_user(found["username"])  
            return
        
        kesempatan -= 1
        print("\nUsername atau password salah!")
        if kesempatan > 0:
            print(f"kesempatan tersisa: {kesempatan}")
            time.sleep(2)
            
    print("Silahkan coba lagi nanti.")            
    time.sleep(3)

# ========================= FUNCTION TOP UP =====================================
def topup(username): 
    header("TOP-UP SALDO DENGAN KODE")
    daftar_paket = load_json('topup.json')
    if not daftar_paket:
        print("Maaf, paket top-up belum tersedia di topup.json.")
        time.sleep(2)
        return
    print("Daftar Paket Top-Up:")
    print("-" * 40)
    for p in daftar_paket:
        print(f"Kode : {p.get('kode')}")
        print(f"Paket: {p.get('nama_paket')}")
        print(f"Harga: Rp{p.get('nominal', 0):,}")
        print("-" * 40)
    users = load_users()
    user = cari_user(users, username)
    print(f"\nSaldo Anda saat ini: Rp{user.get('saldo', 0):,}")
    kode_pilih = input("\nMasukkan Kode Paket (Contoh: L001): ").strip().upper()
    paket_dipilih = None
    for p in daftar_paket:
        if p.get("kode") == kode_pilih:
            paket_dipilih = p
            break
            
    if paket_dipilih is None:
        print("Kode paket tidak valid atau tidak ditemukan!")
        time.sleep(2)
        return
        
    nominal = paket_dipilih.get("nominal", 0)
    user["saldo"] = user.get("saldo", 0) + nominal
    save_users(users)
    
    riwayat_topup = load_json('datatopup.json')
    riwayat_topup.append({
        "username": username,
        "kode_paket": paket_dipilih.get("kode"),
        "nominal": nominal
    })
    save_json('datatopup.json', riwayat_topup)
    
    print(f"\nTop-up berhasil! Paket {paket_dipilih.get('nama_paket')} ditambahkan.")
    print(f"Total saldo Anda sekarang: Rp{user['saldo']:,}")
    time.sleep(3)

def tampilan_katalog(layanan):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Kategori", "Harga", "Estimasi"]
    for s in layanan:
        tabel.add_row([s["id"], s["nama"], s["kategori"], f"Rp{s['harga']:,}", s.get("estimasi", "-")])
    print(tabel)
        
def katalog():
    header("KATALOG LAYANAN")
    layanan = load_json('layanan.json')
    if not layanan:
        print("Belum ada layanan")
    else:
        tampilan_katalog(layanan)
        input("\nTekan Enter untuk kembali......")

def cetak_invoice(t, sisa_saldo):
    header("INVOICE LAUNDRY")
    print("\n" + "="*20 + " STRUK TRANSAKSI " + "="*20)
    print(f"Nama Pelanggan : {t['username']}")
    print(f"ID Transaksi   : {t['id']}")
    print(f"Tanggal        : {t['tanggal']}")
    print("="*56)
    print(f"Layanan        : {t['layanan']}")
    print(f"Jumlah         : {t['jumlah']} {t['satuan']}")
    print(f"Total Harga    : Rp{t['total']:,}")
    print(f"Status         : {t['status_pembayaran']}")
    print(f"Sisa Saldo     : Rp{sisa_saldo:,}")
    print("="*56)
    print("Terima kasih telah menggunakan layanan laundry kami!\n")
    input("Tekan Enter untuk kembali...")

def order(username):
    header("ORDER LAUNDRY")
    layanan = load_json('layanan.json')
    if not layanan:
        print("Belum ada layanan.")
        time.sleep(2)
        return
    tampilan_katalog(layanan) 

    id_pilih = input("\nMasukkan ID layanan: ").strip() 
    if id_pilih == "":
        print("ID layanan tidak boleh kosong.")
        time.sleep(2)
        return

    pilih = None
    for s in layanan:
        if s["id"] == id_pilih:
            pilih = s
            break
    if pilih is None:
        print("ID layanan tidak ditemukan.")
        time.sleep(2)
        return

    try: 
        if pilih["kategori"] == "Kiloan":
            jumlah = float(input("Masukkan berat (kg): ").strip())
            satuan = "kg"
        else:
            jumlah = int(input("Masukkan jumlah layanan: ").strip())
            satuan = "pcs"
    except ValueError:
        print("Input harus berupa angka")
        time.sleep(2)
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0")
        time.sleep(2)
        return

    total = int(round(pilih["harga"] * jumlah)) 

    users = load_json('users.json') 
    user = cari_user(users, username)
    if user is None:
        print("User tidak ditemukan.")
        time.sleep(2)
        return
    if user.get("saldo", 0) < total:
        print(f"Saldo tidak mencukupi. Total Rp{total:,}, saldo Rp{user.get('saldo', 0):,}")
        print("Silahkan top up terlebih dahulu.")
        time.sleep(3)
        return

    print(f"\nRingkasan order: {pilih['nama']} ({jumlah} {satuan})")
    print(f"Total biaya: Rp{total:,}")
    print(f"Sisa saldo setelah transaksi: Rp{user.get('saldo', 0) - total:,}")
    konfirmasi = input("Apakah anda yakin ingin melanjutkan pembayaran? (ya/tidak): ").strip().lower()

    if konfirmasi != "ya": 
        print("\nOrder dbatalkan.")
        time.sleep(2)
        return
    
    user["saldo"] -= total 
    save_json('users.json', users)

    transaksi = load_json('transaksi.json') 
    id_ada = [t["id"] for t in transaksi]
    id_trx = f"TRX-{random.randint(100, 900)}"
    while id_trx in id_ada:
        id_trx = f"TRX-{random.randint(100, 900)}"

    data_baru = { 
        "id": id_trx,
        "username": username,
        "layanan": pilih["nama"],
        "jumlah": jumlah,
        "satuan": satuan,
        "total": total,
        "status_pembayaran": "Lunas",
        "tanggal": time.strftime("%d-%m-%Y %H:%M")
    }

    transaksi.append(data_baru)
    save_json('transaksi.json', transaksi)

    print("Order berhasil! Saldo sudah terpotong otomatis.")
    time.sleep(2)
    cetak_invoice(data_baru, user["saldo"]) 

def riwayat(username):
    header("RIWAYAT TRANSAKSI")
    transaksi = load_json('transaksi.json') 
    milik = [t for t in transaksi if t.get("username") == username]

    if not milik:
        print("Belum ada transaksi.")
        input("\nTekan enter untuk kembali....")
        return

    print("\n" + "="*20 + " STRUK TRANSAKSI " + "="*20) 
    print(f"Nama Pelanggan : {username}")
    print(f"Tanggal Cetak  : {time.strftime('%d-%m-%Y %H:%M:%S')}")
    print("="*56)

    total_semua = 0
    for t in milik:
        print(f"ID Transaksi   : {t.get('id', '-')}")
        print(f"Tanggal        : {t.get('tanggal', '-')}")
        print(f"Layanan        : {t.get('layanan', '-')}")
        print(f"Jumlah         : {t.get('jumlah', 0)} {t.get('satuan', '-')}")
        print(f"Status         : {t.get('status_pembayaran', '-')}")
        print(f"Total Harga    : Rp{t.get('total', 0):,}")
        print("-"*56)
        total_semua += t.get("total", 0)

    print(f"Total Keseluruhan: Rp{total_semua:,}") 
    print("="*56)
    print("Terima kasih telah menggunakan layanan laundry kami!\n")
    input("Tekan Enter untuk kembali...")


def menu_user(username): 
    while True:
        users = load_json('users.json') 
        user = cari_user(users, username)
        saldo = user.get("saldo", 0) if user else 0
        
        header("MENU USER")
        print(f"Selamat datang, {username}!     |   Saldo: Rp{saldo:,}")
        print("="*70)
        print("|    1.  Katalog Layanan                                             |")
        print("|    2.  Top Up Saldo                                                |")
        print("|    3.  Order Laundry                                               |")
        print("|    4.  Riwayat Transaksi                                           |")
        print("|    5.  Logout                                                      |")
        print("="*70)
        
        pilihan = input("Masukkan pilihan yang diinginkan: ").strip()
        
        if pilihan == "1":
            katalog()
        elif pilihan == "2":
            topup(username)
        elif pilihan == "3":
            order(username)
        elif pilihan == "4":
            riwayat(username)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(2)

def menu_utama():
    bersih()
    print("\n"*2)
    print("="*70)
    print("|                          MENU UTAMA LAUNDRY                        |")
    print("="*70)
    print("|    1.  Login                                                       |")
    print("|    2.  Registrasi                                                  |")
    print("|    3.  Keluar                                                      |")
    print("="*70)
while True:  
    menu_utama()
    pilihan = input("Masukkan pilihan yang diinginkan: ")
    if pilihan == "1":
        login()
    elif pilihan == "2":
        regis()
    elif pilihan == "3":
        print("Terima kasih!")
        break
    else: 
        print("Pilihan tidak valid.")
        time.sleep(2)
