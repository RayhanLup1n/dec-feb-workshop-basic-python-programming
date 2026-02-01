# =================================================================
# Python Numbers (int & float)
# =================================================================

# Python itu pintar, dia bisa membedakan antara angka bulat dan angka desimal.
# Kita nggak perlu ribet deklarasi tipenya, Python otomatis tahu.

# =================================================================
# 1. INTEGER (int)
# =================================================================

# int itu bilangan bulat. Tanpa koma sama sekali.
# Cocok buat hitung barang, umur, atau jumlah pengikut di social media.
jumlah_kopi = 3
tahun_ini = 2024

print(f"Jumlah kopi: {jumlah_kopi}, Tipe: {type(jumlah_kopi)}")


# =================================================================
# 2. FLOAT (float)
# =================================================================

# float itu bilangan desimal atau yang ada komanya. 
# Di Python (dan programming pada umumnya), kita pakai TITIK (.) bukan KOMA (,).
# Cocok buat berat badan, suhu, atau harga yang ada sen-nya.
suhu_ruangan = 25.5
berat_badan = 72.0  # Meskipun .0, Python tetap anggap ini float!

print(f"Suhu: {suhu_ruangan}, Tipe: {type(suhu_ruangan)}")


# =================================================================
# 3. RANGE NILAI (DARI KECIL SAMPAI BESAR)
# =================================================================

# Berbeda dengan bahasa lain, 'int' di Python itu luar biasa sakti.
# Dia bisa menampung angka yang SANGAT besar tanpa batas (selama memori komputer cukup).
angka_raksasa = 999999999999999999999999999999
print(f"Angka raksasa tetap aman di Python: {angka_raksasa}")


# =================================================================
# 4. PRIORITAS MATEMATIKA DASAR
# =================================================================

# Meskipun operator ada di file terpisah, ingat kalau Python tetap
# mengikuti aturan matematika (PEMDAS: Kurung, Pangkat, Kali/Bagi, Tambah/Kurang).
hitung = 10 + 2 * 3 
print(f"Hasil 10 + 2 * 3 adalah {hitung} (Bukan 36, tapi 16!)")
