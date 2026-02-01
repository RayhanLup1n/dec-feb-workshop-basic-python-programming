# Practice Time


"""
    Asumsikan kalian adalah seorang programmer di sebuah toko. Kalian diminta untuk
    membuatkan sebuah program simple untuk mengelola stok barang di toko tersebut.

    Program ini akan memiliki beberapa fitur:
    1. Menambahkan barang baru ke dalam stok
    2. Menghapus barang dari stok
    3. Menampilkan daftar barang yang ada di stok
    4. Menghitung total nilai stok

    Data yang akan digunakan:
    - Nama barang (String)
    - Jumlah stok (Integer)
    - Harga satuan (Float)
    
"""

stok_barang = {}

# Function untuk handling penambahan stok
def tambah_stok():
    """
    function yang berfungsi untuk handling penambahan stok.

    Function ini nantinya akan menerima inputan dari user berupa nama barang, jumlah stok dan harganya.
    Hasil dari inputan tersebut akan disimpan ke dalam dictionary stok_barang.

    Args:
        nama (str): Nama barang yang akan ditambahkan.
        jumlah (int): Jumlah stok yang akan ditambahkan.
        harga (float): Harga satuan barang yang akan ditambahkan.
    """

# Function untuk handling penghapusan stok
def hapus_stok():
    """
    Function ini adalah function yang akan menghapus barang dari stok.

    Function ini nantinya akan menerima inputan dari user berupa nama barang yang ingin dihapus.
    Jika barang tersebut ditemukan dalam dictionary stok_barang, maka akan dihapus.
    
    Args:
        nama (str): Nama barang yang akan dihapus.
    """

# Function untuk menampilkan daftar stok
def tampilkan_stok():
    """
    Function ini adalah function yang akan menampilkan daftar stok.

    Function ini nantinya akan menampilkan daftar stok yang ada di dictionary stok_barang.
    Jika stok masih kosong, maka akan menampilkan pesan "Stok masih kosong".

    Function ini tidak akan mengembalikan ataupun menerima inputan apapun.
    Jika function ini dijalankan, hanya akan menampilkan barang yang saat ini ada di dalam dictionary stok_barang.
    """

# Function untuk menghitung total nilai stok
def hitung_total_stok():
    """
    Function ini adalah function yang akan menghitung total nilai stok.

    Function ini nantinya akan menghitung total nilai stok yang ada di dictionary stok_barang.
    Jika stok masih kosong, maka akan menampilkan pesan "Stok masih kosong".
    """

# Function utama untuk menjalankan program
def main():
    """
    Function ini adalah function yang akan menjalankan program.

    Function ini nantinya akan menjalankan program dengan menggunakan while loop.
    """


if __name__ == "__main__":
    main()