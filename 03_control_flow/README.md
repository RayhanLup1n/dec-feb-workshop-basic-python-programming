# 03_control_flow — Mengatur Alur Program

Jika modul-modul sebelumnya mengajarkan kita tentang "benda" (data), modul ini akan mengajarkan kita tentang **"otak"** atau logika dari program.

Program tidak hanya berjalan lurus dari atas ke bawah. Terkadang program harus memilih jalan (Percabangan) atau mengulang pekerjaan yang sama (Perulangan).

---

## 🎯 Tujuan Modul

Setelah menyelesaikan modul ini Anda akan mampu:

- Membuat keputusan dalam kode menggunakan `if`, `elif`, dan `else`
- Mengotomatiskan pekerjaan berulang menggunakan `for` dan `while` loop
- Mengontrol perulangan lebih detail dengan `break` dan `continue`
- Memahami konsep **Indentation** (menjorok ke dalam) yang sangat krusial di Python

---

## 📦 Komponen Utama Control Flow

### 1. Percabangan (Decision Making)
Bayangkan seperti persimpangan jalan. Program akan mengecek sebuah kondisi (Boolean):
- **`if`**: "Jika kondisinya benar, lakukan ini."
- **`else`**: "Jika tidak benar, lakukan itu."
- **`elif`**: "Kalau sebelumnya salah, coba cek kondisi yang satu ini."

### 2. Perulangan (Looping)
Bayangkan seperti lari di stadion. Kamu melakukan hal yang sama berkali-kali:
- **`for` loop**: Digunakan saat kita sudah tahu mau mengulang berapa kali (misal: sebanyak item di dalam List).
- **`while` loop**: Digunakan saat kita mau mengulang **selama** kondisi tertentu masih benar (misal: selama nyawa pemain > 0).

---

## ⚠️ Aturan Emas: Indentasi (Spasi)

Di Python, spasi di awal baris bukan cuma buat tampil rapi. Spasi menentukan **blok kode**.
```python
if True:
    print("Ini masuk dalam blok IF") # Harus menjorok (biasanya 4 spasi)
print("Ini di luar blok IF")
```
Salah indentasi akan menyebabkan `IndentationError`.

---

## 🛠️ Cara Praktis Belajar dari Folder Ini

1. Jalankan script dan amati bagaimana urutan baris kode yang dieksekusi bisa berubah-berubah.
2. Cobalah mengubah nilai variabel kondisi (seperti mengubah angka dari 10 ke 5) dan lihat perbedaannya.
3. Jangan takut terjebak dalam `Infinite Loop` (perulangan selamanya) saat belajar `while`. Jika terjadi, tekan `Ctrl + C` di terminal untuk berhenti.

Mari kita buat program kita menjadi lebih cerdas!

---
