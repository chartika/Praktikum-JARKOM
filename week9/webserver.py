# Import socket module 
from socket import *
import sys # In order to terminate the program 

# Siapkan socket server
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 6789

# Mengikat socket ke alamat (semua interface yang tersedia) dan port 6789
serverSocket.bind(('', serverPort))
# Mulai mendengarkan koneksi masuk (maksimal antrean 1 koneksi)
serverSocket.listen(1)

while True: 
    # Menunggu dan menerima koneksi masuk
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    
    try: 
        # Menerima pesan request dari klien (buffer 1024 byte)
        message = connectionSocket.recv(1024).decode()
        
        # Cetak wujud asli request dari browser ke terminal
        print("\n--- Menerima Request dari Browser ---")
        print(message)
        print("-------------------------------------\n")
        
        # Ekstrak nama file dari pesan HTTP Request
        # (contoh message.split()[1] menghasilkan '/index.html')
        filename = message.split()[1]                
        
        # Buka dan baca isi file yang diminta
        # (menggunakan [1:] untuk membuang karakter '/' di awal nama file)
        f = open(filename[1:])                         
        outputdata = f.read()
        
        # Kirim HTTP header (status 200 OK) ke browser
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode()) 
        
        # Kirim isi file (HTML) ke browser, karakter demi karakter
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 
        
        # Tutup koneksi dengan browser ini
        connectionSocket.close() 
        
        # Cetak pesan sukses di terminal
        print(f"SUKSES File '{filename}' berhasil dikirim ke browser!\n\n")
        
    except IOError: 
        # Jika file tidak ditemukan, masuk ke blok ini
        print(f"GAGAL File '{filename}' tidak ditemukan di server (404).\n\n")
        
        # Kirim HTTP header (status 404 Not Found)
        error_header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(error_header.encode())
        
        # Kirim halaman HTML berisi pesan Error 404 sederhana
        error_body = '<html><body><h1>404 Not Found</h1><p>Maaf, file yang Anda minta tidak ada di server lokal ini.</p></body></html>\r\n'
        connectionSocket.send(error_body.encode())
        
        # Tutup koneksi klien
        connectionSocket.close() 

    serverSocket.close() 
    sys.exit() # Terminate the program after sending the corresponding data