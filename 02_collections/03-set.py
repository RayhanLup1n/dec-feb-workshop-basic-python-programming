# =================================================================
# Python Set: Himpunan yang Unik & Tak Teratur
# =================================================================

# Set adalah koleksi yang isinya TIDAK BOLEH ADA DUPLIKAT.
# Selain itu, Set tidak peduli urutan (Unordered), jadi kita nggak bisa panggil index [0].
# Analoginya seperti sekantong permen: kita nggak tahu mana yang diambil duluan,
# tapi kita cuma peduli rasa apa saja yang ada di sana.

# =================================================================
# 1. CARA BIKIN SET
# =================================================================

# Pakai kurung kurawal { } tanpa key:value.
angka_unik = {1, 2, 3, 4, 4, 4, 5} # Angka 4 yang dobel bakal dibuang otomatis.
print(f"Set angka (otomatis unik): {angka_unik}")

# Hati-hati: {} adalah Dictionary kosong. Kalau mau bikin Set kosong:
set_kosong = set() 


# =================================================================
# 2. MENAMBAH & MENGHAPUS
# =================================================================

numbers = {1, 2, 3}
numbers.add(4)     # Menambah satu item
numbers.update([5, 6, 7]) # Menambah banyak item sekaligus

numbers.remove(1)  # Menghapus angka 1
numbers.discard(10) # Menghapus tapi nggak akan error kalau bendanya nggak ada.

print(f"Isi set sekarang: {numbers}")


# =================================================================
# 3. OPERASI HIMPUNAN (MATEMATIKA)
# =================================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Gabungan (Union) -> Ambil semuanya
print(f"Gabungan: {set_a | set_b}")

# Irisan (Intersection) -> Ambil yang ada di dua-duanya
print(f"Yang sama: {set_a & set_b}")

# Selisih (Difference) -> Ada di A tapi nggak ada di B
print(f"Beda (A-B): {set_a - set_b}")


# =================================================================
# 4. KEGUNAAN NYATA
# =================================================================

# Cara paling cepat buat bersihin data duplikat dari sebuah List.
data_kotor = ["A", "B", "A", "C", "B", "D"]
data_bersih = list(set(data_kotor)) # List -> Set (Unik) -> List kembali

print(f"Data bersih dari duplikat: {data_bersih}")
