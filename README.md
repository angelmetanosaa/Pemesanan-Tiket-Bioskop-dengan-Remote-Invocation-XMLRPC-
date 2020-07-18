# Pemesanan-Tiket-Bioskop-dengan-Remote-Invocation-XMLRPC-
Pemesanan Tiket Bioskop adalah sebuah program sederhana yang kami bangun menggunakan bahasa pemograman Python yang berguna untuk membantu proses transaksi pada pemesanan tiket bisoskop. Program ini dibangun menggunakan teknik Remote Invocation (XMLRPC) yang terdiri dari 2 sisi yaitu Server sebagai penjual dan Client sebagai pembeli. Pada sisi Server yang berperan sebagai penjual, terdapat beberapa fungsi yang dapat dijalankan yaitu :

1. Fungsi info_film() untuk menampilkan info film yang tersedia pada array Slot dan akan dikirimkan ke sisi client
2. Fungsi info_pesanan() untuk melakukan pemesanan tiket dan menghitung total harga yang harus dibayar oleh pembeli
3. Fungsi slot_tiket() untuk mengetahui sisa slot yang tersedia pada setiap filmnya
4. Fungsi main() untuk membuat tampilan menu awal pada server dengan 4 option yaitu : menambahkan film, menghapus film, mengubah harga, dan tidak melakukan perubahan apapun, dengan penjelasan sebagai berikut :

- Menambahkan film berguna untuk menambahkan slot film baru kedalam array Slot oleh penjual, dan info terbaru ini dapat dilihat oleh sisi Client
- Menghapus film berguna untuk menghapus slot film lama di array slot oleh penjual, dan info terbaru ini dapat dilihat oleh sis Client.
- Mengubah harga berguna untuk mengubah harga film dari harga default yaitu Rp35000 menjaid harga inputarn baru secara bebas oleh penjual.
- Tidak melakukan perubahan apa-apa, sehingga program dijalankan sesuai dengan default data yang sudah diberikan sebelumnya.

Pada sisi Client yang berperan sebagai pembeli, terdapat beberapa pemanggilan fungsi yang ada pada sisi Server, yaitu :

1. Menampilkan jadwal film terbaru dan tersedia
2. Memesan tiket bioskop dengan menginputkan pilihan film dan jumlah tiket yang akan dibeli.
3. Melihat harga total tiket yang dibeli.
4. Melihat tampilan tiket akhir yang telah dibeli.

# Instalasi Aplikasi

Tata Cara menjalankan aplikasi Pemesanan Tiket Bioskop
A. Jika dijalankan melalui OS Windows
Buka folder yang didalamnya terdapat 2 file dari program yang dibangun
Membuka CMD (Command Prompt) melalui Address Bar dibagian atas folder dengan mengetikkan kata “cmd” (tanpa tanda petik).

Apa itu CMD? — Command Prompt atau CMD adalah tool command line interface di Windows, yang memungkinkan kamu untuk menjalankan berbagai perintah dan tool yang bahkan tidak tersedia di GUI Windows.
1. Lakukan membuka CMD (Command Prompt) sekali lagi dengan cara yang sama
2. Sekarang, dilayar Anda terdapat 2 kotak CMD.
3. Pada CMD pertama, ketik pembeli.py
4. Pada CMD kedua, ketik penjual.py
5. Tekan enter guna untuk melakukan running program pada CMD pertama yang bertuliskan pembeli.py
6. Selang beberapa waktu kemudian, tekan enter juga guna melakukan running program pada CMD kedua yang bertuliskan penjual.py
7. Pada bagian CMD penjual.py, akan menampilkan 4 option menu yang bisa dipilih oleh penjual, dan akan tersambung secara langsung oleh pembeli sebagai client.
8. Program siap dijalankan, dengan tata cara keseluruhan akan dijelaskan lebih lanjut pada bagian Wiki.
9. Selamat mencoba!

B. Jika dijalankan melalui 0S Linux Ubuntu

1. Buka terminal pertama dengan menekan tombol ctrl+alt pada keyboar ataupun langsung meng-klik menu terminal
2. Buka terminal kedua dengan menekan tombol ctrl+alt
3. Sekarang, dilayar Anda terdapat 2 kotak terminal.
4. Pada kedua terminal, ketik sudo su.
5. Setelah itu, masukkan password linux ubuntu Anda secara benar dikedua terminal.
6. Pada kedua terminal, ketik cd [nama folder tempat tersimpannya file pembeli.py dan penjual.py]
7. Ketik perintah ls, pada kedua terminal untuk mengecek apakah benar kedua file yaitu pembeli.py dan penjual.py ada pada folder tersebut.
8. Jika, ada maka lanjutkan proses selanjutnya. Jika tidak, pastikan Anda benar menyimpan file tersebut pada folder yang sama.
9. Pada terminal pertama, ketik python3 penjual.py
10. Pada terminal kedua, ketik python3 pembeli.py
11. Jalankan terminal pertama (penjual.py) terlebih dahulu dengan menekan tombol enter
12. Selang beberapa detik kemudian, jalankan terminal kedua (pembeli.py) dengan menekan tombol enter
13. Pada bagian terminal penjual.py, akan menampilkan 4 option menu yang bisa dipilih oleh penjual, dan akan tersambung secara langsung oleh pembeli sebagai client.
14. Program siap dijalankan, dengan tata cara keseluruhan akan dijelaskan lebih lanjut pada bagian Wiki.
15. Selamat mencoba!
