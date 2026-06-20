class Buku:
    def __init__(self, jenis):
        self.jenis = jenis
        self.data = []
    def tambah_buku(self):
        judul = input("Judul        : ")
        penulis = input("Penulis      : ")
        tahun = input("Tahun Terbit : ")
        keterangan = input(f"{self.jenis} : ")
        self.data.append([judul, penulis, tahun, keterangan])
        print("Data berhasil ditambahkan!")
    def tampil_buku(self):
        print(f"--- Data {self.jenis} ---")
        if len(self.data) == 0:
            print("Belum ada data.")
        else:
            for i, buku in enumerate(self.data):
                print(
                    f"{i+1}. {buku[0]} | "
                    f"{buku[1]} | "
                    f"{buku[2]} | "
                    f"{buku[3]}"
                )
    def hapus_buku(self):
        self.tampil_buku()
        if len(self.data) > 0:
            nomor = int(input("Nomor yang dihapus : "))
            self.data.pop(nomor - 1)
            print("Data berhasil dihapus!")
class BukuPelajaran(Buku):
    def __init__(self):
        super().__init__("Mata Pelajaran")
        self.data = [
            ["Matematika Dasar", "Budi", "2020", "Matematika"],
            ["Fisika Dasar", "Andi", "2021", "Fisika"],
            ["Algoritma Pemrograman", "Rina", "2022", "Informatika"]
        ]
class Novel(Buku):
    def __init__(self):
        super().__init__("Genre")
        self.data = [
            ["Laskar Pelangi", "Andrea Hirata", "2005", "Drama"],
            ["Bumi", "Tere Liye", "2014", "Fantasi"],
            ["Dilan 1990", "Pidi Baiq", "2014", "Romantis"]
        ]
class Majalah(Buku):
    def __init__(self):
        super().__init__("Edisi")
        self.data = [
            ["National Geographic", "NG Team", "2024", "Januari"],
            ["Tempo", "Tempo Media", "2024", "Februari"],
            ["Bobo", "Redaksi Bobo", "2024", "Maret"]
        ]
class Keanggotaan:
    """Mengelola data anggota perpustakaan."""
    def __init__(self):
        self.anggota = [
            {"id": "A001", "nama": "Andi", "tipe": "Pelajar", "max_hari": 7},
            {"id": "A002", "nama": "Budi", "tipe": "Umum", "max_hari": 14},
            {"id": "A003", "nama": "Citra", "tipe": "Dosen", "max_hari": 30},
        ]
    def tampil_anggota(self):
        print("--- Daftar Anggota ---")
        if not self.anggota:
            print("Belum ada anggota.")
            return
        for i, a in enumerate(self.anggota, 1):
            print(f"{i}. ID: {a['id']} | Nama: {a['nama']} | Tipe: {a['tipe']} | Max Pinjam: {a['max_hari']} hari")
    def tambah_anggota(self):
        id_anggota = input("ID Anggota   : ")
        nama = input("Nama         : ")
        tipe = input("Tipe (Pelajar/Umum/Dosen): ")
        max_hari = int(input("Max Pinjam (hari): "))
        self.anggota.append({"id": id_anggota, "nama": nama, "tipe": tipe, "max_hari": max_hari})
        print("Anggota berhasil ditambahkan!")
    def hapus_anggota(self):
        self.tampil_anggota()
        if self.anggota:
            nomor = int(input("Nomor yang dihapus: "))
            self.anggota.pop(nomor - 1)
            print("Anggota berhasil dihapus!")
    def cari_anggota(self, id_anggota):
        for a in self.anggota:
            if a["id"] == id_anggota:
                return a
        return None
class Peminjaman:
    """Mengelola peminjaman buku dengan durasi."""
    def __init__(self, keanggotaan):
        self.keanggotaan = keanggotaan
        self.pinjam = []
    def pinjam_buku(self, buku_pelajaran, novel, majalah):
        print("--- Peminjaman Buku ---")
        id_anggota = input("ID Anggota: ")
        anggota = self.keanggotaan.cari_anggota(id_anggota)
        if not anggota:
            print("Anggota tidak ditemukan! Daftarkan dulu di menu Keanggotaan.")
            return
        print(f"Anggota: {anggota['nama']} ({anggota['tipe']}) — Max {anggota['max_hari']} hari")
        print("Pilih jenis buku:")
        print("1. Buku Pelajaran")
        print("2. Novel")
        print("3. Majalah")
        jenis = input("Pilih: ")
        if jenis == "1":
            objek = buku_pelajaran
        elif jenis == "2":
            objek = novel
        elif jenis == "3":
            objek = majalah
        else:
            print("Pilihan tidak valid!")
            return
        objek.tampil_buku()
        if len(objek.data) == 0:
            return
        nomor = int(input("Nomor buku yang dipinjam: "))
        if nomor < 1 or nomor > len(objek.data):
            print("Nomor tidak valid!")
            return
        judul = objek.data[nomor - 1][0]
        durasi = int(input(f"Durasi pinjam (hari, max {anggota['max_hari']}): "))
        if durasi > anggota['max_hari']:
            print(f"Durasi melebihi batas! Maksimal {anggota['max_hari']} hari.")
            return
        self.pinjam.append({
            "id_anggota": id_anggota,
            "nama": anggota['nama'],
            "judul": judul,
            "jenis": objek.jenis,
            "durasi": durasi
        })
        print(f"\\n✅ Buku '{judul}' berhasil dipinjam oleh {anggota['nama']} selama {durasi} hari.")
    def tampil_pinjam(self):
        print("\\n=== Daftar Peminjaman ===")
        if not self.pinjam:
            print("Belum ada peminjaman.")
            return
        for i, p in enumerate(self.pinjam, 1):
            print(f"{i}. {p['nama']} | '{p['judul']}' ({p['jenis']}) | {p['durasi']} hari")
    def kembalikan_buku(self):
        self.tampil_pinjam()
        if self.pinjam:
            nomor = int(input("Nomor peminjaman yang dikembalikan: "))
            if 1 <= nomor <= len(self.pinjam):
                p = self.pinjam.pop(nomor - 1)
                print(f"Buku '{p['judul']}' telah dikembalikan oleh {p['nama']}.")
            else:
                print("Nomor tidak valid!")
buku_pelajaran = BukuPelajaran()
novel = Novel()
majalah = Majalah()
keanggotaan = Keanggotaan()
peminjaman = Peminjaman(keanggotaan)
while True:
    print("\\n===== MENU UTAMA =====")
    print("1. Buku Pelajaran")
    print("2. Novel")
    print("3. Majalah")
    print("4. Keanggotaan")
    print("5. Peminjaman Buku")
    print("6. Keluar")
    pilihan = input("Pilih menu : ")
    if pilihan == "1":
        objek = buku_pelajaran
    elif pilihan == "2":
        objek = novel
    elif pilihan == "3":
        objek = majalah
    elif pilihan == "4":
        while True:
            print("--- Menu Keanggotaan ---")
            print("1. Tampilkan Anggota")
            print("2. Tambah Anggota")
            print("3. Hapus Anggota")
            print("4. Kembali")
            aksi = input("Pilih aksi: ")
            if aksi == "1":
                keanggotaan.tampil_anggota()
            elif aksi == "2":
                keanggotaan.tambah_anggota()
            elif aksi == "3":
                keanggotaan.hapus_anggota()
            elif aksi == "4":
                break
            else:
                print("Pilihan tidak valid!")
        continue
    elif pilihan == "5":
        while True:
            print("--- Menu Peminjaman ---")
            print("1. Pinjam Buku")
            print("2. Tampilkan Peminjaman")
            print("3. Kembalikan Buku")
            print("4. Kembali")
            aksi = input("Pilih aksi: ")
            if aksi == "1":
                peminjaman.pinjam_buku(buku_pelajaran, novel, majalah)
            elif aksi == "2":
                peminjaman.tampil_pinjam()
            elif aksi == "3":
                peminjaman.kembalikan_buku()
            elif aksi == "4":
                break
            else:
                print("Pilihan tidak valid!")
        continue
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
        continue
    while True:
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Hapus Buku")
        print("4. Kembali")
        aksi = input("Pilih aksi : ")
        if aksi == "1":
            objek.tambah_buku()
        elif aksi == "2":
            objek.tampil_buku()
        elif aksi == "3":
            objek.hapus_buku()
        elif aksi == "4":
            break
        else:
            print("Pilihan tidak valid!")
'''
with open(output_path, "w", encoding="utf-8") as f:
    f.write(code)

print(f"File berhasil disimpan ke: {output_path}")
'''