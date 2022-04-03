# TucilStima3-BnB
Tugas Kecil 3 IF2211 Strategi Algoritma
Membuat program untuk menyelesaikan 15-puzzle dengan algoritma Branch and Bound

## Cara Kerja Program
1. Mengecek apakah puzzle dapat dislesaikan
2. Jika iya, masukkan puzzle awal ke dalam antrian
3. Memilih puzzle dalam antrian yang memiliki biaya terkecil
4. Mengeksekusi puzzle yang dipilih
5. Ulangi sampai puzzle habis

## Cara Menggunakan Program

### GUI
Buka terminal di folder `src`, kemudian jalankan program dengan mengetikkan perintah berikut di terminal
```
py mainGUI.py
```
Program dengan Graphical User Interface akan muncul. Tekan tombol `Open Puzzle` untuk membuka puzzle dari folder, atau tombol `Get Random Puzzle` untuk mendapatkan puzzle secara acak.
Setelah itu, akan muncul nilai dari SUM(KURANG) + X dari puzzle. Jika puzzle dapat diselesaikan, klik tombol `Solve Puzzle` untuk mencari solusi puzzle. Setelah solusi ketemu, gunakan tombol `Animate` untuk menganimasikan proses penyelesaian puzzle, atau tombol `Next` dan `Prev` untuk menggerakan state puzzle maju atau mundur.

### CLI
Buka terminal di folder `src` kemudian jalankan program dengan mengetikkan perintah berikut ke terminal
```
py main,py
```
Kemudian ikuti instruksi yang diberikan


Atau bisa juga dengan cara beikut
```
py main.py <namafile>
```
Untuk langsung menjalankan program dengan nama file yang diberikan (lengkap dengan ekstensi). File tersebut harus berada di dalam folder `test`

## Author
Rozan Fadhil Al Hafidz 13520039
