# =================================================================
# Python While Loop: Perulangan Selama Kondisinya Benar
# =================================================================

# While Loop digunakan saat kita BELUM TAHU pasti berapa kali mau mengulang.
# Loop ini akan terus berjalan SELAMA kondisinya masih bernilai True.

# =================================================================
# 1. STRUKTUR DASAR
# =================================================================

angka = 1

while angka <= 5:
    print(f"Putaran ke-{angka}")
    # PENTING: Jangan lupa update variabel kondisinya!
    angka += 1 


# =================================================================
# 2. INTERAKSI DENGAN USER
# =================================================================

# While sering dipakai kalau kita nunggu user ngetik perintah tertentu.
perintah = ""

print("\nKetik 'keluar' untuk berhenti.")
while perintah.lower() != "keluar":
    perintah = input("Masukkan perintah: ")
    if perintah.lower() != "keluar":
        print(f"Kamu mengetik: {perintah}")

print("Terima kasih, sampai jumpa!")


# =================================================================
# 3. HATI-HATI: INFINITE LOOP (LOOP SELAMANYA)
# =================================================================

# Ini terjadi kalau kondisinya akan selalu True dan tidak pernah di-update.
# Contoh (JANGAN DIJALANKAN KALAU GAK MAU CPU PANAS):
# while True:
#     print("Bakal jalan selamanya...")

# Tips: Kalau terjebak, tekan Ctrl + C di terminal.


# =================================================================
# 4. GAME SIMPEL (NYAWA PEMAIN)
# =================================================================

nyawa = 3
print("\n--- Game Dimulai ---")

while nyawa > 0:
    print(f"Kamu sedang bertualang... Nyawa tersisa: {nyawa}")
    # Simulasikan terkena jebakan
    nyawa -= 1

print("Game Over! Nyawa habis.")
