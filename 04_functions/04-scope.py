# =================================================================
# Python Function: Variable Scope (Lokal vs Global)
# =================================================================

# Scope menentukan di mana sebuah variabel bisa dikenal atau diakses.
# Ingat: "Apa yang lahir di dalam fungsi, mati di dalam fungsi."

# =================================================================
# 1. VARIABEL LOKAL (LOCAL SCOPE)
# =================================================================

def rahasia():
    pesan_rahasia = "Jangan kasih tahu siapa-siapa!" # Variabel Lokal
    print(f"Di dalam fungsi: {pesan_rahasia}")

rahasia()

# print(pesan_rahasia) ❌ Ini bakal ERROR! 
# Karena variabel tersebut cuma hidup di dalam fungsi rahasia().


# =================================================================
# 2. VARIABEL GLOBAL (GLOBAL SCOPE)
# =================================================================

# Variabel yang dibuat di luar fungsi, bisa dibaca oleh siapa saja (Termasuk fungsi).
kota = "Jakarta" # Variabel Global

def sapa_kota():
    print(f"Saya sedang di {kota}") # Bisa akses variabel luar

sapa_kota()


# =================================================================
# 3. MENGUBAH VARIABEL GLOBAL (GLOBAL KEYWORD)
# =================================================================

skor = 10 

def update_skor():
    # Kalau kita mau ngerubah variabel global dari dalam fungsi,
    # kita harus kasih tahu Python pakai kata kunci 'global'.
    global skor 
    skor = 20
    print(f"Skor di dalam fungsi diubah jadi: {skor}")

print(f"Skor awal: {skor}")
update_skor()
print(f"Skor akhir (berubah): {skor}")


# =================================================================
# PESAN PENTING
# =================================================================
# Hindari terlalu sering pakai variabel global di dalam fungsi jika tidak terpaksa.
# Kebiasaan yang lebih baik adalah mengirim data lewat PARAMETER 
# dan mengambil hasilnya lewat RETURN.
