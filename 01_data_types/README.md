# 01_data_types — Memahami Jenis Data di Python

Dalam pemrograman, kesalahan paling sering bukan karena logika yang rumit,
tetapi karena salah memahami jenis data.

Python tidak menebak maksud Anda — Python memproses nilai dan tipe datanya.
Jika tipe data salah atau diperlakukan keliru, program bisa error atau
menghasilkan output yang tampak benar namun salah secara logika.

---

## 🎯 Tujuan Modul

Setelah menyelesaikan modul ini Anda akan mampu:

- Mengenali ciri-ciri tipe data dasar di Python (`int`, `float`, `complex`, `str`, `bool`)
- Mengetahui kapan menggunakan masing‑masing tipe di konteks nyata
- Menghindari kesalahan umum yang memicu `TypeError` dan bug lain
- Membaca pesan error tipe dengan lebih efektif

Modul ini fokus pada tipe dasar (bukan struktur data seperti list/dict).

---

## 📦 Ringkasan Singkat Tipe Data

- **`int`**: bilangan bulat tanpa desimal. Contoh: 0, -3, 42.
- **`float`**: bilangan desimal. Contoh: 3.14, -0.001.
- **`complex`**: bilangan kompleks dengan bagian real dan imajiner. Contoh: 2+3j.
- **`str`**: teks, diapit oleh tanda kutip. Contoh: "halo", '42'.
- **`bool`**: nilai kebenaran `True` atau `False`.

---

## Detail Per Tipe (ciri, contoh, penggunaan, kesalahan umum)

### `int`

- Ciri: bilangan bulat tanpa koma.
- Contoh: `age = 23`
- Digunakan untuk: hitungan, indeks, umur, jumlah barang.
- Kesalahan umum: mengharapkan pecahan dari pembagian (`/`) — gunakan `float` atau `//` jika ingin bulat.

### `float`

- Ciri: bilangan dengan desimal.
- Contoh: `temperature = 36.6`
- Digunakan untuk: pengukuran, persentase, perhitungan yang butuh pecahan.
- Kesalahan umum: menganggap float selalu presisi — hindari perbandingan langsung dengan `==`.

### `complex`

- Ciri: format `a + bj`.
- Contoh: `z = 1 + 2j`
- Digunakan untuk: komputasi ilmiah, sinyal, pemrosesan tertentu.
- Catatan: perkenalan singkat di modul ini cukup; contoh dan penggunaan lanjutan bisa dijadikan catatan terpisah.

### `str`

- Ciri: teks diapit tanda kutip `'` atau `"`.
- Contoh: `name = "Siti"`
- Digunakan untuk: nama, alamat, pesan, ID non-numerik.
- Kesalahan umum: mengira `"123"` adalah angka; perlu konversi ke `int`/`float` sebelum operasi numerik.

### `bool`

- Ciri: hanya `True` atau `False`.
- Contoh: `is_valid = True`
- Digunakan untuk: kondisi, flag, hasil perbandingan.
- Kesalahan umum: string "True" tidak sama dengan `True` (tipe berbeda).

---

## 🔄 Konversi Tipe (Type Conversion)

Seringkali data datang sebagai string (dari input user, file, atau API). Konversi penting:

```python
num_str = "23"
num = int(num_str)    # 23 (int)
price_str = "19.99"
price = float(price_str)  # 19.99 (float)
```

Selalu validasi input sebelum konversi untuk menghindari `ValueError`.

---

## ⚠️ Kesalahan Umum Pemula

- Menggabungkan tipe berbeda tanpa konversi (mis. `"age: " + 23` akan error)
- Membandingkan float dengan `==` akibat ketidakpresisian
- Mengira string berisi angka otomatis diperlakukan sebagai angka
- Mengabaikan pesan error — baca dan telusuri tipe yang disebutkan

Tip: jika ragu tentang tipe sebuah variabel, gunakan `type(x)` untuk inspeksi cepat.

---

## 🛠️ Cara Praktis Belajar dari Folder Ini

Untuk setiap file `.py` di folder ini:

1. Jalankan file: `python 01_numbers.py`
2. Amati output dan komentar
3. Ubah nilai contoh dan jalankan lagi
4. Tambahkan percobaan sendiri (coba konversi yang berbeda, cek error)

Eksperimen kecil membuat konsep lebih cepat melekat.

---
