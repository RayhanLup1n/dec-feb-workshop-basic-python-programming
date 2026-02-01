# =================================================================
# Python If-Else: Membuat Keputusan
# =================================================================

# Program tidak selalu berjalan lurus. Terkadang dia harus memilih.
# Analogi: "Kalau hari ini hujan, saya bawa payung. Kalau tidak, saya tidak bawa."

# =================================================================
# 1. STRUKTUR DASAR (IF)
# =================================================================

nilai = 85

# Perhatikan titik dua (:) di akhir baris dan INDENTASI (spasi) di baris bawahnya!
if nilai >= 75:
    print("Selamat! Kamu lulus ujian.")


# =================================================================
# 2. IF DAN ELSE (Dua Pilihan)
# =================================================================

usia = 15

if usia >= 17:
    print("Kamu sudah boleh punya SIM.")
else:
    print("Sabar ya, kamu belum cukup umur.")


# =================================================================
# 3. ELIF (Banyak Pilihan)
# =================================================================

# ELIF adalah singkatannya "Else If". Dipakai kalau pilihannya lebih dari dua.
skor = 82

if skor >= 90:
    grade = "A"
elif skor >= 80:
    grade = "B"
elif skor >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Skor kamu {skor}, jadi grademu adalah {grade}")


# =================================================================
# 4. KONDISI BERSARANG (NESTED IF)
# =================================================================

# Ada IF di dalam IF. Dipakai untuk keputusan yang lebih spesifik.
punya_tiket = True
usia_anak = 12

if punya_tiket:
    if usia_anak < 13:
        print("Boleh nonton Film Anak.")
    else:
        print("Boleh nonton Film Remaja.")
else:
    print("Silakan beli tiket dulu di loket.")


# =================================================================
# 5. CARA SINGKAT (TERNARY OPERATOR)
# =================================================================

# Berguna kalau cuma mau pilih satu dari dua nilai secara cepat.
status = "Lulus" if nilai >= 75 else "Gagal"
print(f"Status kamu: {status}")
