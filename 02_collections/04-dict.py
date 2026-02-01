# =================================================================
# Python Dictionary: Data Berlabel (Kamus)
# =================================================================

# Dictionary (Dict) menyimpan data dalam pasangan "Key" (Kunci) dan "Value" (Nilai).
# Alih-alih pakai nomer index [0, 1, 2], kita panggil data pakai namanya (label).
# Analoginya seperti Buku Telepon: Cari "Nama" (Key) buat dapetin "Nomer" (Value).

# =================================================================
# 1. CARA BIKIN DICTIONARY
# =================================================================

# Pakai { key: value }
user = {
    "nama": "Rayhan Resky",
    "pekerjaan": "Data Engineer",
    "usia": 25,
    "is_member": True
}

print(f"Profil User: {user}")
print(f"Tipe data: {type(user)}")


# =================================================================
# 2. MENGAMBIL DATA (BAGAIKAMANA CARA PANGGILNYA?)
# =================================================================

# Cara 1: Kurung siku
print(f"Halo, nama saya {user['nama']}") # Harus pas namanya!

# Cara 2: Pakai .get() -> LEBIH AMAN karena nggak bikin error kalau key-nya nggak ada.
print(f"Hobi: {user.get('hobi', 'Belum mengisi hobi')}")


# =================================================================
# 3. MENAMBAH & MENGUBAH DATA
# =================================================================

# Menambah key baru
user["lokasi"] = "Jakarta"

# Mengubah value lama
user["usia"] = 26

print(f"Update User: {user}")


# =================================================================
# 4. MENGHAPUS DATA
# =================================================================

user.pop("is_member") # Menghapus berdasarkan key
del user["pekerjaan"] # Cara lain menghapus

print(f"Setelah dihapus: {user}")


# =================================================================
# 5. MENGOLEKSI KEY & VALUE
# =================================================================

# Berguna banget kalau nanti kita mau ngakses semua data pakai loop (perulangan)
print(f"Daftar Label (Keys): {list(user.keys())}")
print(f"Daftar Isi (Values): {list(user.values())}")
print(f"Daftar Pasangan: {list(user.items())}")


# =================================================================
# 6. NESTED DICTIONARY (KAMUS DI DALAM KAMUS)
# =================================================================

tim_bola = {
    "id": 101,
    "nama": "Eagle FC",
    "kapten": {
        "nama": "Andi",
        "nomer_punggung": 10
    }
}

print(f"Nama Kapten: {tim_bola['kapten']['nama']}")
