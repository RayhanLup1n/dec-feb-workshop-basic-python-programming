# =================================================================
# Python Function: Return Values
# =================================================================

# Ada dua jenis fungsi:
# 1. Yang cuma 'beraksi' (seperti print).
# 2. Yang 'memberi hasil' kembali ke kita (pakai return).

# =================================================================
# 1. PERBEDAAN PRINT VS RETURN
# =================================================================

def aksi_print(a, b):
    print(a + b) # Cuma tampilin di layar, nggak bisa disimpan buat dihitung lagi.

def aksi_return(a, b):
    return a + b # Mengirimkan hasil keluar dari fungsi.

# Mari kita lihat bedanya
hasil_1 = aksi_print(5, 5) # Muncul 10 di layar
print(f"Isi variabel hasil_1: {hasil_1}") # Isinya 'None' (Karena nggak ada return)

hasil_2 = aksi_return(10, 10) # Nggak muncul apa-apa di layar
print(f"Isi variabel hasil_2: {hasil_2}") # Isinya 20! Bisa dipakai lagi.


# =================================================================
# 2. RETURN UNTUK PERHITUNGAN
# =================================================================

def hitung_luas_persegi(sisi):
    return sisi * sisi

luas_meja = hitung_luas_persegi(5)
luas_lantai = hitung_luas_persegi(10)

total_luas = luas_meja + luas_lantai
print(f"Total luas: {total_luas}")


# =================================================================
# 3. RETURN BANYAK NILAI SEKALIGUS (TUPLE UNPACKING)
# =================================================================

# Di balik layar, Python membungkus nilai-nilai yang dipisahkan koma menjadi TUPLE.
def kalkulator_simple(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    return tambah, kurang, kali # Langkah 1: Python membungkusnya jadi (15, 5, 50)

# Langkah 2: UNPACKING (Membongkar Paket)
# Nilai akan dimasukkan ke variabel sesuai urutan kembaliannya.
# hasil_tambah = isi pertama (tambah)
# hasil_kurang = isi kedua (kurang)
# hasil_kali   = isi ketiga (kali)
hasil_tambah, hasil_kurang, hasil_kali = kalkulator_simple(10, 5)

print(f"H.Tambah: {hasil_tambah}")
print(f"H.Kurang: {hasil_kurang}")
print(f"H.Kali  : {hasil_kali}")

# Kalau kita cuma pakai satu variabel penampung, maka dia akan jadi Tuple utuh:
semua_hasil = kalkulator_simple(10, 5)
print(f"Hasil utuh (Tuple): {semua_hasil}")
