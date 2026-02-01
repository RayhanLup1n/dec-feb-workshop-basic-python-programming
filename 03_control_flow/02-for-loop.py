# =================================================================
# Python For Loop: Perulangan Terencana
# =================================================================

# For Loop digunakan saat kita tahu persis berapa kali mau mengulang,
# atau saat kita mau mengunjungi setiap item di dalam sebuah koleksi (List, Tuple, dll).

# =================================================================
# 1. MENGULANG LIST (ITERASI)
# =================================================================

buah_buahan = ["Apel", "Mangga", "Jeruk", "Pisang"]

print("Daftar Buah:")
for buah in buah_buahan:
    # Variabel 'buah' akan otomatis berubah isinya di setiap putaran
    print(f"- Saya suka makan {buah}")


# =================================================================
# 2. MENGGUNAKAN RANGE()
# =================================================================

# range(stop) -> Mulai dari 0 sampai (stop - 1)
print("\nHitung sampai 5:")
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

# range(start, stop)
print("\nAngka 10 sampai 15:")
for i in range(10, 16):
    print(i)


# =================================================================
# 3. MENGULANG STRING
# =================================================================

nama = "DEC"
print("\nEja Nama:")
for huruf in nama:
    print(huruf)


# =================================================================
# 4. MENGULANG DICTIONARY
# =================================================================

profil = {"nama": "Rayhan", "jabatan": "Engineer"}

print("\nDetail Profil:")
for kunci, isi in profil.items():
    print(f"{kunci.capitalize()}: {isi}")


# =================================================================
# 5. NESTED LOOP (LOOP DI DALAM LOOP)
# =================================================================

# Hati-hati, ini bisa bikin program jadi berat kalau datanya banyak.
print("\nTabel Perkalian Kecil (1-3):")
for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris} x {kolom} = {baris * kolom}")
    print("---") # Pemisah antar baris
