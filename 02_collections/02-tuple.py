# =================================================================
# Python Tuple: Koleksi yang "Anti-Ganti"
# =================================================================

# Tuple mirip sekali dengan List, tapi punya satu perbedaan besar:
# Tuple bersifat IMMUTABLE (Tidak bisa diubah setelah dibuat).
# Analoginya seperti Piagam atau Akte Kelahiran: sekali terbit, datanya tetap.

# =================================================================
# 1. CARA BIKIN TUPLE
# =================================================================

# Pakai kurung biasa ( ) atau bahkan tanpa kurung pun bisa.
koordinat = (10, 20)
warna_rgb = ("Red", "Green", "Blue")

# Tuple dengan satu item saja? Harus pakai koma di akhir!
angka_tunggal = (5,) 

print(f"Koordinat: {koordinat}")
print(f"Tipe data: {type(koordinat)}")


# =================================================================
# 2. KENAPA PAKAI TUPLE?
# =================================================================

# 1. Aman: Data tidak sengaja terhapus atau terubah di tengah kode.
# 2. Cepat: Python memproses Tuple lebih cepat daripada List.

# koordinat[0] = 100 ❌ Ini bakal ERROR karena Tuple nggak bisa diubah.


# =================================================================
# 3. MENGAMBIL DATA
# =================================================================

# Caranya sama persis dengan List.
print(f"Warna pertama: {warna_rgb[0]}")
print(f"Warna terakhir: {warna_rgb[-1]}")


# =================================================================
# 4. UNPACKING TUPLE (MEMBONGKAR ISI)
# =================================================================

# Kita bisa langsung masukkan isi tuple ke variabel terpisah.
biodata = ("Budi", 25, "Jakarta")
nama, usia, kota = biodata

print(f"Nama: {nama}, Usia: {usia}, Kota: {kota}")


# =================================================================
# 5. BERAPA BANYAK ISINYA?
# =================================================================

numbers = (1, 2, 2, 3, 4, 2)
print(f"Berapa kali angka 2 muncul? {numbers.count(2)}")
print(f"Panjang tuple: {len(numbers)}")
