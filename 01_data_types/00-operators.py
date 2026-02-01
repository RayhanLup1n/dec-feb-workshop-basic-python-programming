# =================================================================
# Python Operators: Alat Bantu Olah Data
# =================================================================

# Operator itu seperti simbol bantuan untuk memproses data. 
# Mulai dari hitung-hitungan sampai banding-bandingin nilai.

# =================================================================
# 1. OPERATOR ARITMATIKA (HITUNG-HITUNGAN)
# =================================================================

# Digunakan untuk melakukan operasi matematika dasar:
# (+) Penjumlahan : Menjumlahkan dua nilai.
# (-) Pengurangan : Mengurangkan nilai pertama dengan nilai kedua.
# (*) Perkalian   : Mengalikan dua nilai.
# (/) Pembagian   : Membagi nilai (hasilnya selalu angka desimal/float).
# (//) Bagi Bulat : Membagi dan membuang angka di belakang koma (pembulatan ke bawah).
# (%) Modulo      : Mengambil sisa dari hasil pembagian.
# (**) Pangkat    : Memangkatkan angka (eksponen).

a = 10
b = 3

print("--- Aritmatika ---")
print(f"10 + 3  = {a + b}")    # 13
print(f"10 - 3  = {a - b}")    # 7
print(f"10 * 3  = {a * b}")    # 30
print(f"10 / 3  = {a / b}")    # 3.333...
print(f"10 // 3 = {a // b}")   # 3
print(f"10 % 3  = {a % b}")    # 1
print(f"10 ** 3 = {a ** b}")   # 1000


# =================================================================
# 2. OPERATOR PERBANDINGAN (CEK KONDISI)
# =================================================================

# Digunakan untuk membandingkan dua nilai. Hasilnya cuma True atau False:
# (==) Sama dengan          : True jika kedua nilai sama.
# (!=) Tidak sama dengan    : True jika kedua nilai berbeda.
# (>)  Lebih besar          : True jika nilai kiri lebih besar dari kanan.
# (<)  Lebih kecil          : True jika nilai kiri lebih kecil dari kanan.
# (>=) Lebih besar sama dengan : True jika nilai kiri lebih besar atau sama dengan kanan.
# (<=) Lebih kecil sama dengan : True jika nilai kiri lebih kecil atau sama dengan kanan.

x = 5
y = 10

print("\n--- Perbandingan ---")
print(f"Apakah {x} == {y}? {x == y}")
print(f"Apakah {x} != {y}? {x != y}")
print(f"Apakah {x} > {y}?  {x > y}")
print(f"Apakah {x} <= {y}? {x <= y}")


# =================================================================
# 3. OPERATOR LOGIKA (GABUNG KONDISI)
# =================================================================

# Digunakan untuk menghubungkan beberapa hasil perbandingan:
# (and) Dan : Menghasilkan True jika SEMUA kondisi bernilai True.
# (or)  Atau: Menghasilkan True jika SALAH SATU kondisi bernilai True.
# (not) Tidak: Membalikkan nilai (True jadi False, dan sebaliknya).

punya_tiket = True
punya_uang = False

print("\n--- Logika ---")
print(f"Boleh masuk bioskop? (Tiket AND Uang): {punya_tiket and punya_uang}") # False
print(f"Boleh masuk bioskop? (Tiket OR Uang) : {punya_tiket or punya_uang}")  # True
print(f"Apakah beneran gak punya tiket? (NOT Tiket): {not punya_tiket}")     # False


# =================================================================
# 4. OPERATOR PENUGASAN (ASSIGNMENT)
# =================================================================

# Digunakan untuk memberikan atau memperbarui nilai ke dalam variabel:
# (=)  Sama dengan : Mengisi nilai ke variabel.
# (+=) Tambah sama dengan : Menambah nilai lama dengan nilai baru.
# (-=) Kurang sama dengan : Mengurang nilai lama dengan nilai baru.

skor = 10
print("\n--- Assignment ---")
print(f"Skor awal: {skor}")

skor += 5  # Sama saja dengan: skor = skor + 5
print(f"Skor setelah (+= 5): {skor}")

skor -= 2  # Sama saja dengan: skor = skor - 2
print(f"Skor setelah (-= 2): {skor}")
