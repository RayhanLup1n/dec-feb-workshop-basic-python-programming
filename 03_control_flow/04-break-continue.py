# =================================================================
# Python Break & Continue: Navigasi di Tengah Perulangan
# =================================================================

# Terkadang kita nggak mau nunggu loop sampai selesai secara normal.
# Kita butuh "tombol darurat" (Break) atau "tombol skip" (Continue).

# =================================================================
# 1. BREAK (BERHENTI PAKSA)
# =================================================================

# Break langsung keluar dari seluruh perulangan, bodo amat sisa antriannya.
print("--- Simulasi Antrian ---")
antrian = ["Budi", "Siti", "Anto", "Sari", "Rudi"]

for orang in antrian:
    if orang == "Anto":
        print(f"Lho, {orang} ternyata bawa bom! TUTUP TOKONYA!")
        break # Langsung keluar dari loop for
    print(f"Melayani pelanggan: {orang}")


# =================================================================
# 2. CONTINUE (LEWATI SAJA)
# =================================================================

# Continue cuma 'skip' putaran sekarang, dan lanjut ke putaran berikutnya.
print("\n--- Filter Pesan Masuk ---")
pesan_masuk = ["Halo", "Spam: Pinjaman Online", "Meeting jam 2", "Spam: Menang Undian", "Apa kabar?"]

for pesan in pesan_masuk:
    if "Spam" in pesan:
        # "Eh, ini pesan sampah, skip aja ke pesan selanjutnya!"
        continue 
    print(f"Membaca pesan: {pesan}")


# =================================================================
# 3. PENGGUNAAN PADA WHILE LOOP
# =================================================================

print("\n--- Masukkan Password ---")
while True:
    pw = input("Ketik password (rahasia): ")
    if pw == "rahasia":
        print("Akses diterima!")
        break # Keluar dari loop 'while True' yang tadinya selamanya
    else:
        print("Salah! Coba lagi.")


# =================================================================
# 4. PASS (CUMA FORMALITAS)
# =================================================================

# Pass dipakai kalau kamu butuh bikin struktur kode tapi belum tahu isinya apa.
# Supaya Python nggak error karena blok kodenya kosong.
if True:
    pass # "Nanti aja diisi, yang penting jalan dulu."

print("\nProgram selesai tanpa hambatan!")
