#import time
import time

# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client dengan ip localhot dan port sebesar 8012
server = xmlrpc.client.ServerProxy('http://localhost:8012')

# lakukan pemanggilan fungsi info() untuk mengetahui jadwal film terbaru yang dikirimkan dari server(penjual)
jadwal = server.info()

#untuk menampilkan jadwal terbaru
for i in jadwal :
    print(i)

print("===============================================")

#membuat variable untuk melakukan input pilih film yang tersedia
tkt =int(input("Pilih Film =  "))
#membuat variable untuk melakukan input jumlah tiket yang tersedia dengan maks 5 slot
aa = int(input("Jumlah Tiket = "))

#melakukan pemanggilan fungsi pesanan yang ada pada server, sehingga bisa menjumlahkan total harga dari jmlh film yg diinputkan
harga = server.pesanan(tkt,aa)
#menampilkan harga total
print("Harga Total = Rp", harga)

#melakukan pemanggilan fungsi slot yg ada pada server sehingga mengetahui sisa slot yang tersedia pada film yg dipilih
slott = server.slot(tkt,aa)
#menampilkan sisa slot film yang dipilih
print("Sisa Slot Film dipilih = ", slott)
#untuk memberikan jeda waktu selama 3 detik sebelum menampilkan fungsi yang lain
time.sleep(3)

#menampilkan tampilan tiket
print("===============================================")
print("             CINEMA XXI                ")

#jika film yang dipilih nomor 1, maka sistem akan menampilkan nama film yg dipilih,total tiket yg dipesan, dan total harga 
if(tkt==1):
    print("FILM = ", jadwal[tkt-1][0])
    print("JUMLAH TIKET = ", aa)
    print("HARGA = Rp",harga)

#jika film yang dipilih nomor 2, maka sistem akan menampilkan nama film yg dipilih,total tiket yg dipesan, dan total harga
elif(tkt==2):
    print("FILM = ",jadwal[tkt-1][0])
    print("JUMLAH TIKET = ", aa)
    print("HARGA = Rp",harga)
    
#jika film yang dipilih nomor 3, maka sistem akan menampilkan nama film yg dipilih,total tiket yg dipesan, dan total harga
elif(tkt==3):
    print("FILM = ",jadwal[tkt-1][0])
    print("JUMLAH TIKET = ", aa)
    print("HARGA = Rp",harga)
    
#jika film yang dipilih nomor 4, maka sistem akan menampilkan nama film yg dipilih,total tiket yg dipesan, dan total harga
elif(tkt==4):
    print("FILM = ",jadwal[tkt-1][0])
    print("JUMLAH TIKET = ", aa)
    print("HARGA = Rp",harga)

#jika film yang dipilih tidak ada pada info film, maka outputnya adalah "FILM TIDAK TERSEDIA" 
else:
    print("         FILM TIDAK TERSEDIA")
print("===============================================")