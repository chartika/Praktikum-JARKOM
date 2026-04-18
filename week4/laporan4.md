# Laporan Praktikum Jaringan Komputer
Nama    : Chartika Jenyansa Pangaribuan
NIM     : 103072400026

## Tujuan Praktikum
Mempelajari lebih lanjut cara kerja DNS menggunakan Wireshark dan CMD

## Langkah Percobaan
### Nslookup
Pertanyaan:
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP server tersebut?
2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?

Jawaban:
1. Domain yang digunakan adalah www.ui.ac.id dengan Alamat IP (IPv4) adalah 152.118.147.93
![Hasil Percobaan](../assets/image/week4/1.png)
2. Berdasarkan hasil analisis, diperoleh beberapa server DNS otoritatif untuk domain ox.ac.uk, yaitu dns0.ox.ac.uk, dns1.ox.ac.uk, dns2.ox.ac.uk, auth4.dns.ox.ac.uk, auth5.dns.ox.ac.uk, dan auth6.dns.ox.ac.uk. Hasil yang ditampilkan berstatus Non-authoritative answer, yang berarti informasi berasal dari cache DNS lokal, namun tetap valid untuk mengidentifikasi nameserver domain tersebut. Hal ini menunjukkan bahwa domain ox.ac.uk menggunakan beberapa server DNS untuk meningkatkan keandalan dan distribusi beban dalam proses resolusi nama domain.
![Hasil Percobaan](../assets/image/week4/2.png)
3. Berdasarkan hasil analisis, diperoleh informasi bahwa domain yahoo.com memiliki beberapa mail exchanger yaitu mta6.am0.yahoodns.net, mta7.am0.yahoodns.net, dan mta5.am0.yahoodns.net dengan prioritas yang sama. Meskipun sempat terjadi DNS request timed out, hasil tetap berhasil diperoleh dan berstatus Non-authoritative answer, yang berarti data berasal dari cache DNS, namun tetap valid. Hal ini menunjukkan bahwa Yahoo menggunakan beberapa server email untuk meningkatkan keandalan dan distribusi beban dalam layanan pengiriman email.
![Hasil Percobaan](../assets/image/week4/3.png)

### Ipconfig
1. ketika memberikan perintah ipconfig pada CMD, maka akan menampilkan informasi konfigurasi jaringan pada komputer yang meliputi TCP/IP termasuk alamat IP anda, alamat server DNS dan lainnya.
![Hasil Percobaan](../assets/image/week4/4.png)
2. untuk perintah ipconfig /all akan memunculkan nama device atau host name dan informasi lengkap mengenai konfigurasi jaringan yang digunakan oleh komputer.
![Hasil Percobaan](../assets/image/week4/5.png)
3. ipconfig /displaydns, akan menampilkan informasi DNS yang tersimpan pada komputer, menampilkan record dan sisa Time To Live (TTL).
![Hasil Percobaan](../assets/image/week4/6.png)
4. ipconfig /flushdns. berfungsi untuk mengosongkan catatan DNS dalam artian akan menghapus seluruh record dan memebuat ulang record dari file.
![Hasil Percobaan](../assets/image/week4/7.png)

### Tracing DNS dengan Wireshark
Langkah-langkah percobaan:
1. Gunakan ipconfig untuk mengosongkan catatan DNS di host
2. Buka browser dan kosongkan cachenya
3. Buka wireshark dan masukkan "ip.addr == 10.218.5.143" pada filter
4. Mulai pengambilan paket pada wireshark
5. Buka URL berikut http://www.ietf.org/ pada browser anda
6. Hentikan pengambilan paket

Pertanyaan:
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP
atau TCP?
- Jawaban: berdasarkan hasil capturing, pesan permintaan dan pesan balasan DNS dikirim menggunakan protokol UDP dengan destination 53, yang merupakan port standart untuk layanan DNS
![Hasil Percobaan](../assets/image/week4/8.png)
2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?
- Jawaban: port tujuan pada permintaan DNS adalah 53 sedangkan port sumber pada balasannya adalah 63531
![Hasil Percobaan](../assets/image/week4/8.png)
3. Pada permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda (gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama?
- Jawaban: alamat IP tujuan dan dan alamat IP server DNS lokal sama
![Hasil Percobaan](../assets/image/week4/9.png)
4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan permintaan tersebut mengandung ”jawaban” atau ”answers”?
- Jawaban: pesan permintaan DNS merupakan type A dan pesan permintaan tersebut tidak mengandung jawaban atau answer (answer=0)
![Hasil Percobaan](../assets/image/week4/10.png)
5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?
- Jawaban: answers pada pesan balasan DNS adalah 2. kedua jawaban tersebut berisi alamat IP www.eitf.org yaitu 104.16.44.99 dan 104.16.45.99
![Hasil Percobaan](../assets/image/week4/11.png)
6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?
- Jawaban: 