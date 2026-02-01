# =================================================================
# Python Function: Dasar-Dasar
# =================================================================

# Fungsi adalah sebuah blok kode yang hanya akan berjalan ketika dipanggil.
# Kita menggunakannya untuk membungkus perintah yang sering kita pakai berulang kali.

# =================================================================
# 1. CARA MENDIFINISIKAN FUNGSI (DEF)
# =================================================================

# Gunakan kata kunci 'def' diikuti nama fungsi dan kurung ().
# Dan jangan lupa TITIK DUA (:) serta INDENTASI.

def sapa_dunia():
    """Ini adalah docstring (Opsional): Menjelaskan fungsi ini buat apa."""
    print("Halo dunia! Saya sedang belajar Function.")
    print("Keren ya, kode ini dibungkus supaya rapi.")


# =================================================================
# 2. CARA MEMANGGIL FUNGSI
# =================================================================

# Setelah didefinisikan, fungsi nggak bakal jalan sendiri.
# Kita harus panggil namanya.

print("--- Sebelum panggil fungsi ---")
sapa_dunia() # Panggil sekali
sapa_dunia() # Panggil dua kali
print("--- Sesudah panggil fungsi ---")


# =================================================================
# 3. KENAPA HARUS PAKAI FUNGSI?
# =================================================================

# Bayangkan kalau kita mau ganti teks sapaannya.
# Kalau kita copas kode manual 10 kali, kita harus ganti 10 kali juga.
# Tapi dengan fungsi, kita cukup ganti isinya di satu tempat saja!

def info_program():
    print("Versi Program: 1.0.0")
    print("Dibuat oleh: Tim DEC")

# Panggil kapan pun kita butuh info ini
info_program()
