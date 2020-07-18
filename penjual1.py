# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

#import threading
import threading

#import OS
import os

#import time
import time

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

# Buat server
server = SimpleXMLRPCServer(("localhost",8012), requestHandler=RequestHandler)
server.register_introspection_functions()

#membuat array untuk menampung slot setiap filmnya
slot = [["Sebelum Iblis Menjemput", 5],["Milea 1990", 5],["Invesible Man", 5]]
harga1 = 35000

#membuat fungsi info film yang tersedia
def info_film():
    print("==================================================================================")
    print("Info Film yang Tersedia = ", slot)
    print("==================================================================================")
    return slot

#membuat register fungsi info_film dengan nama info
server.register_function(info_film, "info")

#membuat fungsi info_pesanan untuk melakukan pemesanan
def info_pesanan(tkt,aa):
    harga = harga1*aa
    #melakukan print info film yang di;ilih, jumlah tiket, dan harga total dari pesanan pada client
    print("==================================================================================")
    print("Film yang Dipilih = ", tkt)
    print("Jumlah Tiket = ", aa)
    print("Harga Total = ", harga)
    print("==================================================================================")
    #return tkt
    #return aa
    return harga

#membuat register fungsi info_pesanan dengan nama pesanan
server.register_function(info_pesanan, "pesanan")

#membuat fungsi untuk mengetahui slot yang tersedia pada setiap filmnya 
def slot_tiket(x,y):
    if (x==1):
        slot[x-1][1]=slot[x-1][1]-y
    elif (x==2):
        slot[x-1][1]=slot[x-1][1]-y
    elif (x==3):
        slot[x-1][1]=slot[x-1][1]-y
    elif (x==4):
        slot[x-1][1]=slot[x-1][1]-y 
    else :
        print("SLOT TIDAK TERSEDIA")     
    print("==================================================================================")
    print("Sisa Slot dari Film yang dipilih : ", slot)
    print("==================================================================================")
    return slot[x-1][1]

#membuat register fungsi slot tiket dengan nama slot
server.register_function(slot_tiket, "slot")

#fungsi untuk membuat tampilan menu awal pada server dengan 4 option
def main():
    print("========================================")
    print("Tekan 1 Untuk Tambah Film")
    print("Tekan 2 Untuk Hapus Film")
    print("Tekan 3 Untuk Ganti Harga")
    print("Tekan 4 Untuk Tambah Film Flashsale")
    print("Tekan 5 Jika Tidak ada Perubahan")
    print("========================================")
    #penjual menginputkan pilihan yang akan dipilih 
    menu = int(input("Masukkan pilihan menu: "))
    return menu   
#untuk menjalankan fungsi main() 
mainmenu = main()


tambahslot = 5
tambahfilm = str(input("Tambah Nama Film = "))
#harga default per-film yaitu 35.000

def flashsale ():
    b = [tambahfilm, tambahslot]
    slot.append(b)
    
    #return harga1

if mainmenu == 1:
    #tambahfilm = str(input("Tambah Nama Film = "))
    #tambahslot = 5
    #membuat variable untuk array baru yang akan dimasukkan ke array slot
    a = [tambahfilm,tambahslot]
    #menggabungkan array baru ke array slot
    slot.append(a)

#untuk pilihan 2, penjual memilih nomor film yang akan dihapus
elif mainmenu == 2:
    hapusfilm = int(input("Pilih Nomor Film yang Akan dihapus = "))
    #menghapus film yang sudah dipilih dari array slot
    slot.pop(hapusfilm-1)
    #untuk menampilkan slot terbaru
    for i in slot :
        print(i)

#untuk pilihan 3, penjual akan mengubah harga default dengan harga inputan baru
elif mainmenu == 3 :
    gantiharga = int(input("Masukkan Harga Baru = "))
    #harga1 adalah harga default yg akan diganti dengan harga terbaru
    harga1 = gantiharga

elif mainmenu == 4 :
    flashsale()
    gantihargafs = int(input("Masukkan Harga Baru = "))
    #harga1 adalah harga default yg akan diganti dengan harga terbaru
    harga1 = gantihargafs

elif mainmenu ==5 :
    pass
else :
    #untuk pilihan 4, maka akan dijalankan seperti biasa tanpa ada perubahan data apapun
    print("INPUTAN YANG ANDA MASUKKAN SALAH! SILAHKAN COBA LAGI")
    time.sleep(1)
    os.system("cls")
    main()
 
#membuat register fungsi main dengan nama mainmenu  
server.register_function(main, "mainmenu")

#menjalankan server seterusnya
server.serve_forever()