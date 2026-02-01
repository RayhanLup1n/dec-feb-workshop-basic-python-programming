# =================================================================
# Python Type Conversion: Mengubah Wujud Data
# =================================================================

# Kadang data yang kita punya nggak sesuai sama yang kita butuhin.
# Contohnya: Kita dapet angka "25" tapi wujudnya Teks (String),
# eh tiba-tiba kita mau tambahin sama angka 5. Harus kita ubah dulu wujudnya!

# =================================================================
# 1. KE INTEGER (int)
# =================================================================

teks_angka = "100"
angka_asli = int(teks_angka) # Mengubah string jadi angka bulat

print(f"Hasil: {angka_asli + 50}") # Berhasil jadi 150!


# =================================================================
# 2. KE FLOAT (float)
# =================================================================

berat_str = "65.5"
berat_float = float(berat_str) # Mengubah string jadi angka desimal

print(f"Berat: {berat_float} kg")


# =================================================================
# 3. KE STRING (str)
# =================================================================

# Ini sering dipakai pas kita mau gabungin angka ke dalam kalimat.
skor = 100
pesan = "Skor kamu adalah " + str(skor)
print(pesan)


# =================================================================
# 4. KE BOOLEAN (bool)
# =================================================================

# Mengubah nilai apa pun menjadi True atau False (Konsep Truthy/Falsy).
print(f"Apakah angka 1 itu True? {bool(1)}")
print(f"Apakah string kosong itu True? {bool('')}")


# =================================================================
# 5. DARI FLOAT KE INT (BUANG DESIMAL)
# =================================================================

# Mengubah float ke int akan membuang angka di belakang koma (bukan membulatkan).
ipk = 3.99
ipk_bulat = int(ipk) # Hasilnya jadi 3

print(f"IPK asli: {ipk}, Diubah ke int: {ipk_bulat}")
