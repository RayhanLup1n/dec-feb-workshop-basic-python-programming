# =================================================================
# Python List: Daftar yang Bisa Berubah
# =================================================================

# List adalah koleksi data yang paling sering dipakai di Python.
# Mirip seperti daftar belanja atau daftar nama siswa: urutannya jelas 
# dan kita bisa menambah atau menghapus barang di dalamnya kapan saja.

# =================================================================
# 1. CARA BIKIN LIST
# =================================================================

# Pakai kurung siku [ ] dan pisahkan item dengan koma.
hobiku = ["Membaca", "Ngoding", "Lari", "Makan"]
random_data = ["Rayhan", 25, True, 3.14] # List bisa nampung campuran tipe data!

print(f"Daftar hobi: {hobiku}")
print(f"Tipe data: {type(hobiku)}")


# =================================================================
# 2. MENGAMBIL DATA (INDEXING & SLICING)
# =================================================================

# Ingat: Indeks dimulai dari 0.
print(f"Hobi pertama: {hobiku[0]}")
print(f"Hobi terakhir: {hobiku[-1]}")
print(f"Dua hobi pertama: {hobiku[0:2]}")


# =================================================================
# 3. MENAMBAH & MENGUBAH DATA (MUTABLE)
# =================================================================

# List bersifat MUTABLE, artinya isinya bisa kita acak-acak sesuka hati.

# Menambah di akhir
hobiku.append("Berenang")

# Mengubah data yang sudah ada
hobiku[0] = "Belajar" # "Membaca" diganti jadi "Belajar"

print(f"Daftar hobi terbaru: {hobiku}")


# =================================================================
# 4. MENGHAPUS DATA
# =================================================================

# Pakai .remove() kalau tahu nama barangnya
hobiku.remove("Makan")

# Pakai .pop() kalau mau hapus index tertentu (atau yang terakhir kalau kosong)
hobiku.pop(1) # Hapus indeks 1

print(f"Setelah dihapus: {hobiku}")


# =================================================================
# 5. METODE LIST LAINNYA
# =================================================================

angka = [5, 2, 8, 1, 9]
angka.sort() # Mengurutkan angka dari kecil ke besar
print(f"Angka urut: {angka}")
angka.sort(reverse=True)
print(f"Angka urut: {angka}")

huruf = ["A", "B", "A", "C"]
print(f"Jumlah huruf A: {huruf.count('A')}")
print(f"Panjang list: {len(huruf)}")
