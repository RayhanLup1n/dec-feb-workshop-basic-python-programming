# 04_functions — Menulis Kode yang Reusable & Rapi

Selamat datang di modul **Functions**! Jika sebelumnya kita menulis kode secara berurutan, sekarang kita akan belajar membungkus kode tersebut ke dalam sebuah "wadah" yang bisa kita panggil kapan saja.

Analogi: Fungsi itu seperti **resep masakan**. Kamu cuma butuh menulis resepnya sekali, tapi kamu bisa memasak hidangan tersebut berkali-kali hanya dengan memanggil namanya.

---

## 🎯 Tujuan Modul

Setelah menyelesaikan modul ini Anda akan mampu:

- Memahami konsep **DRY (Don't Repeat Yourself)** dalam pemrograman
- Membuat fungsi sendiri menggunakan kata kunci `def`
- Mengirimkan data ke dalam fungsi menggunakan **Parameters & Arguments**
- Mengambil hasil olahan fungsi menggunakan kata kunci `return`
- Memahami perbedaan antara variabel **Local** dan **Global** (Scope)

---

## 📦 Kenapa Kita Butuh Fungsi?

### 1. Menghindari Duplikasi
Daripada menulis 10 baris kode yang sama di 5 tempat berbeda, lebih baik masukkan ke dalam satu fungsi. Jika ada perubahan, kamu cuma perlu ubah di satu tempat.

### 2. Kode Lebih Terstruktur
Fungsi membantu memecah masalah besar menjadi potongan-potongan kecil yang lebih mudah dikelola dan dibaca.

### 3. Kemudahan Debugging
Jika ada error, kamu tahu persis fungsi mana yang bermasalah.

---

## 🧩 Anatomi Sebuah Fungsi

```python
def sapa_user(nama):          # 'nama' adalah PARAMETER (input)
    """Ini adalah docstring (penjelasan singkat fungsi)"""
    print(f"Halo, {nama}!")   # Isi fungsi

sapa_user("Rayhan")           # "Rayhan" adalah ARGUMENT (nilai asli)
```

---

## 🛠️ Cara Praktis Belajar dari Folder Ini

1. Perhatikan perbedaan antara fungsi yang cuma **mencetak** sesuatu (`print`) dengan fungsi yang **mengembalikan** nilai (`return`).
2. Cobalah buat fungsi yang menerima lebih dari satu parameter.
3. Eksperimen: Apa yang terjadi jika kamu memanggil variabel yang dibuat di dalam fungsi dari luar fungsi? (Spoiler: Ini tentang *Scope*).
4. Jangan lupa untuk selalu memberikan nama fungsi yang deskriptif (gunakan kata kerja, misal: `hitung_total`, bukan cuma `hitung`).

Mari kita mulai merapikan kode kita dengan Functions!

---
