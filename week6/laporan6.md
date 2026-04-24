# Laporan Praktikum Jaringan Komputer
Nama    : Chartika Jenyansa Pangaribuan
NIM     : 103072400026

## Tujuan Praktikum
Menginvestigasi cara kerja protokol TCP menggunakan Wireshark

## Langkah Percobaan
### Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server 
1. Buka URL Buka http://gaia.cs.umass.edu/wireshark-labs/alice.txt (pastikan harus http bukan https).
![Hasil Percobaan](../image/week6/1.png)

2. Salin seluruh teks ke notepad dan simpan dalam bentuk format txt
![Hasil Percobaan](../image/week6/2.png)

3. Setelah itu buka URL http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html
![Hasil Persobaan](../image/week6/3.png)

4. Pilih "choose file" dan masukkan file Alice yang sudah disimpan sebelumnya
![Hasil Percobaan](../image/week6/4.png)

5. Mulai capture wireshark, tunggu beberapa saat lalu pilih "upload file"
![Hasil Percobaan](../image/week6/5.png)

6. Stop capturing packets, maka tampilan wireshark akan seperti ini
![Hasil Percobaan](../image/week6/6.png)

### Tampilan Awal pada Captured Trace
1. Download Trace zip pada http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip lalu ekstrak
2. Cari file tcp-ethereal-trace-1 lalu tambahkan pcap dibagian belakangnya (tcp-ethereal-trace-1.pcap) agar bisa dibuka di wireshark
![Hasil Percobaan](../image/week6/7.png)
3. Buka file tersebut di wireshark, lalu filter menjadi protokol TCP. maka akan muncul Three-way hanshake seperti ini
![Hasil Percobaan](../image/week6/8.png)

Pertanyaan:
1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk mentransfer file ke gaia.cs.umass.edu? Cara paling mudah menjawab pertanyaan ini adalah dengan memilih sebuah pesan HTTP dan meneliti detail paket TCP yang digunakan untuk membawa pesan HTTP tersebut
2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini?

Jawaban:
1. Alamat IP komputer klien adalah 192.168.1.102 dan nomor port TCP yang digunakan adalah 1161 untuk mentransfer data ke server gaia.cs.umass.edu
2. Alamat IP dari gaia.cs.umass.edu adalah 128.119.245.12. Server menggunakan nomor port 80 untuk mengirim dan menerima segmen TCP dalam koneksi ini

### HTML Documents dengan Embedded Objects
Pertanyaan:
1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN?
2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen sehingga teridentifikasi sebagai segmen SYNACK?
3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATAnya.
4. Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut?Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar JARINGAN KOMPUTER 36 paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time Graph).
5. Berapa panjang setiap enam segmen TCP pertama?
6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah menghambat pengiriman?
7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di dalam file trace) untuk menjawab pertanyaan ini?

Jawaban:
1. Sesuai dengan yang didapatkan segmen TCP pertama memiliki relative sequence number 0. Segmen ini diidentifikasi sebagai segmen SYN karena bagian TCP Flag terdapat tanda 'Syn: Set' dengan nilai Flag 0x002.
Segmen ini dapat diidentifikasi sebagai segmen SYN karena memiliki flag SYN yang aktif, yang berfungsi untuk memulai koneksi TCP dalam proses three-way handshake.
![Hasil percobaan](../image/week6/9.png)
2. Pada segmen SYN-ACK (paket ke-2) nilai relative sequence number yang digunakan server adalah 0, sedangkan nilai Acknowledgment number adalah 1. Nilai acknowledgment ini diperoleh dari nilai sequence number klien sebelumnya (0) ditambah 1, sehingga pada gambar nilai Next Sequence Number adalah 1. 
Segmen ini diidentifikasi sebagai SYN-ACK karena memiliki kedua flag SYN dan ACK yang aktif, yang menunjukkan bahwa segmen tersebut merupakan balasan dari permintaan koneksi sekaligus konfirmasi penerimaan SYN dari klien.
![Hasil percobaan](../image/week6/10.png)
3. Berdasarkan analisis trace pada paket nomor 199, segmen TCP yang membawa perintah HTTP POST memiliki relative sequence number sebesar 164041. Segmen ini merupakan bagian awal dari pengiriman data dari klien ke server setelah koneksi TCP terbentuk, sehingga sequence number tersebut digunakan sebagai acuan dalam proses transfer data TCP.
![Hasil percobaan](../image/week6/11.png)
4. Segmen pertama yang digunakan sebagai acuan adalah segmen HTTP POST pada frame 199 dengan sequence number 164041 dan waktu pengiriman 5.297341 detik. Acknowledgment untuk segmen tersebut diterima pada frame 203 dengan waktu 5.461175 detik, sehingga diperoleh nilai RTT sebesar sekitar 0.16 detik.
Berdasarkan grafik Round Trip Time, terlihat bahwa nilai RTT untuk segmen-segmen berikutnya berada pada kisaran sekitar 0.1 hingga 0.27 detik dan membentuk pola naik turun (zig-zag). Hal ini menunjukkan adanya variasi delay jaringan selama proses komunikasi.
Nilai Estimated RTT diperoleh dari rata-rata bergerak nilai RTT yang terukur. Karena nilai RTT pada grafik relatif stabil dalam rentang tersebut, maka Estimated RTT juga cenderung stabil dan berada di sekitar 0.16–0.2 detik.
![Hasil Percobaan](../image/week6/12.png)
![Hasil Percobaan](../image/week6/13.png)
5. Panjang enam segmen TCP pertama bervariasi, terlihat dari field Len pada trace, yaitu terdapat segmen dengan panjang 50 byte, 1460 byte, dan 272 byte. Nilai ini menunjukkan ukuran payload TCP pada masing-masing segmen yang dikirim dari klien ke server.
6. Berdasarkan nilai Window Size pada trace, ruang buffer minimum yang disarankan oleh penerima berada di kisaran 17520 byte (dari klien) dan hingga 62780 byte (dari server). Nilai ini menunjukkan kapasitas buffer penerima untuk menerima data sebelum harus mengirim acknowledgment. Selama proses komunikasi, tidak terlihat adanya nilai window yang turun menjadi nol, sehingga dapat disimpulkan bahwa tidak terjadi keterbatasan buffer penerima yang menghambat pengiriman data.
![Hasil Percobaan](../image/week6/14.png)
7. Dengan menggunakan filter tcp.analysis.retransmission pada Wireshark, tidak ditemukan adanya paket yang ditandai sebagai retransmission. Hal ini terlihat dari hasil filter yang menunjukkan tidak ada paket yang ditampilkan (0 packet). Selain itu, tidak terdapat indikasi seperti “TCP Retransmission” atau “Fast Retransmission” pada daftar paket. Dengan demikian, dapat disimpulkan bahwa tidak terjadi retransmisi segmen TCP selama proses komunikasi, sehingga koneksi berlangsung dengan baik tanpa adanya kehilangan paket.
![Hasil Percobaan](../image/week6/15.png)