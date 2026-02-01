# =================================================================
# Python Boolean: Benar atau Salah?
# =================================================================

# Boolean adalah tipe data yang cuma punya dua nilai: True atau False.
# Ini adalah jantung dari logika pemrograman. Kalau nggak ada Boolean,
# komputer nggak bakalan tahu kapan harus 'Lanjut' atau 'Berhenti'.

# =================================================================
# 1. DEFINISI BOOLEAN
# =================================================================

semangat_belajar = True
mau_nyerah = False

# Ingat: Kapital di awal itu wajib (True/False).
print(f"Apakah semangat? {semangat_belajar}")
print(f"Tipe data: {type(semangat_belajar)}")


# =================================================================
# 2. APA ITU TRUTHY & FALSY?
# =================================================================

# Di Python, benda yang "Kosong" atau "Nol" biasanya dianggap False (Falsy).
# Benda yang "Ada isinya" dianggap True (Truthy).

print("--- Contoh Falsy (Dianggap False) ---")
print(f"Striing kosong ('')  : {bool('')}")
print(f"Angka nol (0)        : {bool(0)}")
print(f"Kosong sama sekali   : {bool(None)}")

print("\n--- Contoh Truthy (Dianggap True) ---")
print(f"String ada isinya ('Oke') : {bool('Oke')}")
print(f"Angka selain nol (10)     : {bool(10)}")
print(f"Spasi saja (' ')         : {bool(' ')}") # Jangan terkecoh, spasi itu ada isinya!
