# 02_collections — Mengelola Grup Data di Python

Jika pada modul sebelumnya kita belajar menyimpan satu nilai dalam satu variabel (seperti satu kotak untuk satu barang), pada modul ini kita akan belajar tentang **Collections**.

Collections memungkinkan kita menyimpan **banyak data dalam satu tempat**. Di dunia nyata, ini seperti daftar belanja, rak buku, atau buku kontak di handphone Anda.

---

## 🎯 Tujuan Modul

Setelah menyelesaikan modul ini Anda akan mampu:

- Membedakan penggunaan 4 tipe data koleksi utama: `list`, `tuple`, `set`, dan `dict`
- Mengetahui kapan harus menggunakan koleksi yang bisa diubah (mutable) vs yang tidak (immutable)
- Mengakses dan mengolah data di dalam koleksi menggunakan index atau key
- Memilih struktur data yang paling efisien untuk kebutuhan program Anda

---

## 📦 Ringkasan Tipe Data Koleksi

| Tipe Data | Ciri Utama | Kegunaan Utama |
| :--- | :--- | :--- |
| **`list`** | Terurut, bisa diubah, mengizinkan duplikat. | Daftar item yang urutannya penting (mis. antrian). |
| **`tuple`** | Terurut, **tidak bisa diubah**, mengizinkan duplikat. | Data yang harus tetap/aman (mis. koordinat GPS). |
| **`set`** | Tidak terurut, unik (tidak boleh ada duplikat). | Mencari nilai unik atau operasi himpunan. |
| **`dict`** | Pasangan *Key:Value*, sangat cepat untuk pencarian. | Data berlabel (mis. profil user, spek barang). |

---

## Detail Per Koleksi

### `list` (Daftar)
- Ciri: Menggunakan kurung siku `[]`.
- Contoh: `fruits = ["Apel", "Mangga", "Jeruk"]`
- Digunakan untuk: Menyimpan kumpulan data yang urutannya ingin kita jaga dan isinya bisa kita tambah/hapus.

### `tuple` (Grup Tetap)
- Ciri: Menggunakan kurung biasa `()`.
- Contoh: `point = (10, 20)`
- Digunakan untuk: Data yang sekali dibuat tidak boleh berubah selama program jalan. Lebih hemat memori dibanding list.

### `set` (Himpunan Unik)
- Ciri: Menggunakan kurung kurawal `{}` tanpa pasangan key-value.
- Contoh: `ids = {101, 102, 103}`
- Digunakan untuk: Menghilangkan data duplikat secara otomatis.

### `dict` (Kamus/Dictionary)
- Ciri: Menggunakan kurung kurawal `{}` dengan format `key: value`.
- Contoh: `user = {"nama": "Budi", "umur": 25}`
- Digunakan untuk: Menyimpan data yang punya label, sehingga kita tidak perlu repot menghafal urutan index-nya.

---

## 🛠️ Cara Praktis Belajar dari Folder Ini

Untuk setiap file `.py` yang akan Anda pelajari:

1. Amati cara data dimasukkan ke dalam koleksi (simbol kurungnya berbeda-beda!)
2. Pelajari cara mengambil satu data spesifik dari dalamnya
3. Cobalah untuk menambah atau menghapus data dan lihat koleksi mana yang mengizinkannya
4. Eksperimen: coba masukkan tipe data yang berbeda (misal memasukkan `list` di dalam `dict`)

Ingat: Memilih struktur data yang tepat adalah langkah awal menjadi programmer yang efisien!

---
