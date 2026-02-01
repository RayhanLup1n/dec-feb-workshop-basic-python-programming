# =================================================================
# Python String
# =================================================================

# Bayangkan String itu seperti "kalimat" atau "teks" yang kita pakai setiap hari.
# Di dunia programming, hampir semua yang kita lihat di layar adalah String.
# Contohnya:
# - Nama lengkap Anda di profil LinkedIn
# - Alamat email buat login
# - Chat yang Anda kirim di WhatsApp
# - Bahkan data yang kita ambil dari Excel atau Database

# =================================================================
# 1. CARA BIKIN STRING
# =================================================================

# Cukup bungkus teks Anda dengan tanda kutip. Boleh dua ("") atau satu ('').
message = "Halo, calon programmer hebat!"
print(message)
print(type(message))  # OUTPUT: <class 'str'>


# =================================================================
# 2. CIRI KHAS STRING
# =================================================================

# 1. Bisa diisi apa saja: huruf, angka, simbol (#!@), sampai spasi pun dihitung.
# 2. String itu IMMUTABLE. Maksudnya? Teks yang sudah dibuat tidak bisa
#    diubah isinya secara langsung. Kalau mau ganti, kita harus buat "variabel baru".


# =================================================================
# 3. KENAPA IMMUTABLE PENTING?
# =================================================================

text = "python"

# text[0] = "P"  ❌ Ini bakal bikin Python marah (Error).
# Kita nggak bisa main ganti huruf di tengah jalan seperti itu.

# Solusinya? Kita olah teksnya, lalu simpan ke variabel (bisanya variabel yang sama).
text = text.capitalize() 
print(text)  # Nah, sekarang jadi "Python". Yang lama sudah diganti yang baru.


# =================================================================
# 4. JURUS-JURUS STRING (METHODS) YANG WAJIB TAHU
# =================================================================

# Kenapa kita butuh ini? Karena data dari user itu seringkali "berantakan".
raw_input = "   user@email.com   " 

# 1. .strip() -> Buat "bersihin" spasi nggak sengaja di awal & akhir. 
clean_email = raw_input.strip()
print(f"Email bersih: '{clean_email}'")

# 2. .upper() & .lower() -> Menyamakan format (misal buat pencarian data).
print(clean_email.upper())
print(clean_email.lower())

# 3. .replace() -> Ganti kata tertentu dalam teks.
announcement = "Belajar Java itu seru!"
print(announcement.replace("Java", "Python"))

# 4. .split() -> Pisahkan teks berdasarkan separator.
announcement = "Belajar Java itu seru!"
print(announcement.split(" "))

# 5. .join() -> Gabungkan teks dengan separator.
words = ["Belajar", "Java", "itu", "seru!"]
announcement = " ".join(words)
print(announcement)

# 6. .capitalize() -> Ubah huruf pertama menjadi kapital.
announcement = "belajar java itu seru!"
print(announcement.capitalize())

# 7. .title() -> Ubah huruf pertama setiap kata menjadi kapital.
announcement = "belajar java itu seru!"
print(announcement.title())

# =================================================================
# 5. CARA GABUNGIN TEKS (CONCATENATION)
# =================================================================

first_name = "Rayhan"
last_name = "Resky"

# Menggunakan operator (+)
print(first_name + last_name)

# Menggunakan comma (,)
print(first_name, last_name)

# =================================================================
# 6. MENGAMBIL POTONGAN TEKS (INDEXING & SLICING)
# =================================================================

# Kadang kita cuma butuh sebagian data saja.
# Format menggunakan slicing adalah [Start:Stop:Step].
# Python adalah bahasa zero-indexed based, artinya semua indexing selalu dimulai dari angka 0.

date = "2024-02-01" 

# Contoh Real: Kita cuma mau ambil TAHUN-nya saja.
year = date[0:4] # Ambil dari indeks 0, sebanyak 4 karakter.
print(f"Tahun transaksi: {year}")

# Negatif Index
# Digunakan untuk mengambil data dari belakang.
# Untuk negatif index, angknya dimulai dari -1.
print(f"Karakter terakhir dari tanggal: {date[-1]}")


# =================================================================
# 7. CARA CEK ISI TEKS (MEMBERSHIP TEST)
# =================================================================

email_user = "kontak@belajarcoding.id"

print("@" in email_user)          # Output: True (Berarti format email-nya ada @-nya)
print("yahoo" in email_user)      # Output: False


# =================================================================
# 8. INTERAKSI DENGAN USER (INPUT)
# =================================================================

# Ingat: Apapun yang diketik user lewat input(), tipenya SELALU String.
hobby = input("Apa hobi kamu pas lagi santai? ")
print(f"Wih, {hobby} seru banget tuh buat refreshing!")


# =================================================================
# 9. KARAKTER KHUSUS (ESCAPE CHARACTER)
# =================================================================

# Kadang kita butuh simbol yang "bentrok" sama syntax Python.
# Gunakan backslash (\) sebagai tanda "Eh Python, ini teks biasa ya, bukan kode".

print("Dia bilang: \"Belajar Python itu investasi masa depan.\"")
print("Baris satu\nBaris dua (ini ganti baris otomatis)")

