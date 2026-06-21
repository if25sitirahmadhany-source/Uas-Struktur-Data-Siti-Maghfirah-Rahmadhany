#Aplikasi Manajemen Perpustakaan Berbasis CSV dengan Menggunakan Hash Map dan Queue 

import csv
import os
from collections import deque

FILE_BUKU = "Perpustakaan.csv"

# Queue untuk antrian peminjaman
antrian = deque()

# Membuat file CSV jika belum ada
if not os.path.exists(FILE_BUKU):
    with open(FILE_BUKU, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Judul", "Pengarang", "Stok"])


# =====================================
# HASH MAP
# =====================================
def load_hash_map():
    hash_map = {}

    with open(FILE_BUKU, mode="r") as file:
        reader = csv.reader(file)

        next(reader)  # lewati header

        for row in reader:
            hash_map[row[0]] = {
                "judul": row[1],
                "pengarang": row[2],
                "stok": row[3]
            }

    return hash_map


# =====================================
# CREATE
# =====================================
def tambah_buku():
    print("\n=== TAMBAH BUKU ===")

    id_buku = input("ID Buku      : ")

    # Cek ID sudah ada atau belum
    hash_map = load_hash_map()

    if id_buku in hash_map:
        print("ID Buku sudah digunakan!")
        return

    judul = input("Judul Buku   : ")
    pengarang = input("Pengarang    : ")
    stok = input("Stok         : ")

    with open(FILE_BUKU, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id_buku, judul, pengarang, stok])

    print("Data berhasil ditambahkan!")


# =====================================
# READ
# =====================================
def lihat_buku():
    print("\n=== DAFTAR BUKU ===")

    with open(FILE_BUKU, mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        ada_data = False

        for row in reader:
            ada_data = True

            print(f"""
ID        : {row[0]}
Judul     : {row[1]}
Pengarang : {row[2]}
Stok      : {row[3]}
----------------------------
""")

        if not ada_data:
            print("Belum ada data buku.")


# =====================================
# SEARCHING (HASH MAP)
# =====================================
def cari_buku():
    print("\n=== CARI BUKU ===")

    id_buku = input("Masukkan ID Buku: ")

    hash_map = load_hash_map()

    if id_buku in hash_map:
        buku = hash_map[id_buku]

        print("\nBuku ditemukan!")
        print("ID        :", id_buku)
        print("Judul     :", buku["judul"])
        print("Pengarang :", buku["pengarang"])
        print("Stok      :", buku["stok"])

    else:
        print("Buku tidak ditemukan!")


# =====================================
# UPDATE
# =====================================
def ubah_buku():
    print("\n=== UBAH BUKU ===")

    id_buku = input("Masukkan ID Buku yang akan diubah: ")

    data = []
    ditemukan = False

    with open(FILE_BUKU, mode="r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] == "ID":
                data.append(row)
                continue

            if row[0] == id_buku:
                ditemukan = True

                print("\nMasukkan Data Baru")

                row[1] = input("Judul Baru     : ")
                row[2] = input("Pengarang Baru : ")
                row[3] = input("Stok Baru      : ")

            data.append(row)

    with open(FILE_BUKU, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    if ditemukan:
        print("Data berhasil diubah!")
    else:
        print("Buku tidak ditemukan!")


# =====================================
# DELETE
# =====================================
def hapus_buku():
    print("\n=== HAPUS BUKU ===")

    id_buku = input("Masukkan ID Buku yang akan dihapus: ")

    data = []
    ditemukan = False

    with open(FILE_BUKU, mode="r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] == id_buku:
                ditemukan = True
                continue

            data.append(row)

    with open(FILE_BUKU, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    if ditemukan:
        print("Data berhasil dihapus!")
    else:
        print("Buku tidak ditemukan!")


# =====================================
# SORTING
# =====================================
def sortir_buku():
    print("\n=== SORTIR BUKU ===")

    with open(FILE_BUKU, mode="r") as file:
        data = list(csv.reader(file))

    header = data[0]
    isi = data[1:]

    isi.sort(key=lambda x: x[1].lower())

    with open(FILE_BUKU, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(isi)

    print("Data berhasil diurutkan berdasarkan judul!")


# =====================================
# TAMPILKAN HASH MAP
# =====================================
def tampil_hash_map():
    print("\n=== HASH MAP BUKU ===")

    hash_map = load_hash_map()

    if not hash_map:
        print("Data kosong")
        return

    for key, value in hash_map.items():
        print(f"{key} -> {value}")


# =====================================
# QUEUE (ANTRIAN PEMINJAMAN)
# =====================================
def tambah_antrian():
    print("\n=== TAMBAH ANTRIAN ===")

    nama = input("Nama Peminjam : ")
    id_buku = input("ID Buku       : ")

    antrian.append((nama, id_buku))

    print("Berhasil masuk antrian!")


def lihat_antrian():
    print("\n=== DAFTAR ANTRIAN ===")

    if len(antrian) == 0:
        print("Antrian kosong!")
    else:
        for i, data in enumerate(antrian, start=1):
            nama, id_buku = data
            print(f"{i}. {nama} - {id_buku}")


def layani_antrian():
    print("\n=== LAYANI ANTRIAN ===")

    if len(antrian) == 0:
        print("Antrian kosong!")
    else:
        nama, id_buku = antrian.popleft()
        print(f"{nama} meminjam buku {id_buku}")


# =====================================
# MENU
# =====================================
while True:

    print("\n")
    print("=" * 40)
    print(" SISTEM MANAJEMEN PERPUSTAKAAN ")
    print("=" * 40)
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Cari Buku (Hash Map)")
    print("4. Ubah Buku")
    print("5. Hapus Buku")
    print("6. Sortir Buku")
    print("7. Tampilkan Hash Map")
    print("8. Tambah Antrian")
    print("9. Lihat Antrian")
    print("10. Layani Antrian")
    print("0. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        tambah_buku()

    elif pilihan == "2":
        lihat_buku()

    elif pilihan == "3":
        cari_buku()

    elif pilihan == "4":
        ubah_buku()

    elif pilihan == "5":
        hapus_buku()

    elif pilihan == "6":
        sortir_buku()

    elif pilihan == "7":
        tampil_hash_map()

    elif pilihan == "8":
        tambah_antrian()

    elif pilihan == "9":
        lihat_antrian()

    elif pilihan == "10":
        layani_antrian()

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
