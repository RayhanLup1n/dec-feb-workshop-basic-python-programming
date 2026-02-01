# =================================================================
# Python Complex Numbers
# =================================================================

# Bilangan kompleks mungkin jarang kita lihat di aplikasi sehari-hari,
# tapi buat ilmuwan atau teknisi, ini adalah makanan sehari-hari.

# =================================================================
# 1. CARA BIKIN BILANGAN KOMPLEKS
# =================================================================

# Terdiri dari bagian Real dan Imajiner (ditandai dengan 'j').
z1 = 3 + 4j
z2 = complex(2, -5) # Menghasilkan 2-5j

print(f"Bilangan Kompleks 1: {z1}")
print(f"Bilangan Kompleks 2: {z2}")
print(f"Tipe data: {type(z1)}")


# =================================================================
# 2. NGINTIP ISI BAGIANNYA
# =================================================================

# Kita bisa ambil masing-masing bagiannya secara terpisah.
# Ingat: Hasilnya bakal selalu bertipe 'float'.
z = 10 + 7j

print(f"Bagian Real: {z.real}")
print(f"Bagian Imajiner: {z.imag}")


# =================================================================
# 3. CONJUGATE (KEBALIKAN TANDA)
# =================================================================

# Berguna untuk membalikkan tanda di bagian imajinernya saja.
angka = 4 + 3j
print(f"Konjugat dari {angka} adalah {angka.conjugate()}")
