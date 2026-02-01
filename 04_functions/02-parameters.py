# =================================================================
# Python Function: Parameters & Arguments
# =================================================================

# Fungsi akan jadi lebih sakti kalau kita bisa kirim data ke dalamnya.
# Parameter = "Variabel penampung" (saat bikin fungsi).
# Argument  = "Nilai asli" yang kita kirim (saat panggil fungsi).

# =================================================================
# 1. SATU PARAMETER
# =================================================================

def sapa_personaly(nama):
    print(f"Halo {nama}, selamat datang di Komunitas DEC!")

sapa_personaly("Rayhan")
sapa_personaly("Budi")


# =================================================================
# 2. BANYAK PARAMETER
# =================================================================

def perkenalan(nama, hobi, usia):
    print(f"Nama saya {nama}, hobi saya {hobi}, dan usia saya {usia} tahun.")

# Urutan pengiriman harus sama dengan urutan di definisinya
perkenalan("Rayhan", "Ngoding", 25)


# =================================================================
# 3. DEFAULT PARAMETER
# =================================================================

# Kita bisa kasih "nilai cadangan" kalau user lupa kirim data.
def absen_siswa(nama, kelas="Python Dasar"):
    print(f"Siswa: {nama} | Kelas: {kelas}")

absen_siswa("Siti") # 'kelas' otomatis jadi 'Python Dasar'
absen_siswa("Andi", "Data Enginner") # 'kelas' berubah jadi 'Data Engineer'


# =================================================================
# 4. KEYWORD ARGUMENTS
# =================================================================

# Kalau parameternya banyak dan kita takut tertukar urutannya,
# kita bisa sebutkan namanya pas panggil.
def kirim_paket(penerima, kurir, berat):
    print(f"Kirim ke: {penerima} | Kurir: {kurir} | Berat: {berat}kg")

# Meskipun urutannya acak, Python tetap tahu karena kita sebut namanya.
kirim_paket(kurir="JNE", berat=2, penerima="Sari")
