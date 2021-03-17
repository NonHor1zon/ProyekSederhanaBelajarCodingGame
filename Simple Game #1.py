#Pengembangan Simple Game #1
'''
Pengembang :

- NonHor1zon (Github)

'''
#---------------------
'''
Catatan :

Merupakan pengembangan dari Simple Game #1 dengan Command Yang Lebih Mendalam

'''
#---------------------
'''
DaftarNamaVariabel - Jawab
'''
JawabA = "A"
JawabB = "B"
JawabC = "C"
JawabD = "D"
JawabYa = "Ya"
JawabTidak = "Tidak"
JawabKiri = "Kiri"
JawabKanan = "Kanan"
JawabAtas = "Atas"
JawabBawah = "Bawah"
JawabLakukan = "Lakukan"
JawabJangan = "Jangan"
JawabSetuju = "Setuju"
JawabTolak = "Tolak"
#---------------------
'''
DaftarNamaVariabel - Awal
'''
JawabAwal_Mulai = "Mulai"
JawabAwal_Kredit = "Kredit"
JawabAwal_Keluar = "Keluar"
#---------------------
'''
Status Awal
'''
Stamina = 80
Kesehatan = 100
Haus = 50
Lapar = 50
#---------------------
'''
Start Menu Awal, Mulai
'''
def StartMenu1():
    print ("Halo, Selamart Datang di 'Reruntuhan Tua'")
    print ("Silahkan Masukkan Namamu")
    NamaPemain = input('')
    print ('Halo' + ' ' + NamaPemain)
def StartMenu2():
    print ('Silahkan Memilih Antara Berikut')
    print ('Mulai/Kredit/Keluar')
    JawabMenuAwal = input('Jawab : ')
    if JawabMenuAwal == JawabAwal_Mulai :
        print('Mari Kita Mulai')
        print('')
        print('')
        MulaiGame()
    elif JawabMenuAwal == JawabAwal_Kredit :
        print("Kredit:")
        print('- NonHor1zon (Github)')
        StartMenu2()
    elif JawabMenuAwal == JawabAwal_Keluar :
        print("Apakah Anda Yakin?")
        YakinKeluar = input("Ya/Tidak : ")
        if YakinKeluar == JawabYa:
            exit()
        elif YakinKeluar == JawabTidak:
            StartMenu2()
        else:
            StartMenu2()
    else :
        StartMenu2()
'''
Start Menu Awal, Selesai
'''
#---------------------
'''
Poin Karakter
'''
PoinBeruang = 1
#---------------------
'''
Gameplay Part 1, Mulai
'''
def MulaiGame():
    print ('Kamu Menjelajahi Hutan')
    print ('Kamu Merasa Lelah Dan Haus')
    print ('Selain Itu Hari Sudah Sore')
    print ('Kamu Menemukan Reruntuhan Kuno di Tengah Hutan')
    print ('Apa Yang Akan Kamu Lakukan?')
    print ('A. Masuk Ke Reruntuhan')
    print ('B. Cari Sumber Air')
    print ('C. Menunggu Hingga Malam')
    print ('D. Membuat Tenda')
    KetemuReruntuhan()
def KetemuReruntuhan():
    global Stamina
    Jawab_KetemuReruntuhan = input ('Jawab: ')
    if Jawab_KetemuReruntuhan == JawabA :
        print("Kamu Memasuki Reruntuhan")
        print("Tepat Setelah Kamu Memasukinya, Pintu Masuk Reruntuhan Tersebut Mulai Runtuh")
        print("Namanya Juga Reruntuhan :)")
        EnterLanjut_1()
    elif Jawab_KetemuReruntuhan == JawabB :
        print("Kamu Mencari Sumber Air, Namun Kamu Tidak Dapat Menemukannya")
        print("Stamina -10")
        Stamina -= 10
        print("Kamu Memilih Untuk Memasuki Reruntuhan")
        print("Seketika Setelah Kamu Masuk, Pintu Reruntuhan Mulai Runtuh")
        print('Kamu Bergumam Dalam Hati "Ada Alasan Tempat Ini Disebut Reruntuhan"')
        EnterLanjut_1()
    elif Jawab_KetemuReruntuhan == JawabC :
        print("Kamu Beristirahat Hingga Malam Tiba")
        print("Kamu Tertidur Dengan Pulas Di Atas Rumput")
        print("Ketika Kamu Bangun, Waktu Sudah Berjalan Sekitar 2 Jam")
        print("Stamina + 20")
        Stamina += 20
        print("Pada Akhirnya Kamu Memutuskan Untuk Masuk Ke Dalam Reruntuhan")
        EnterLanjut_1()
    elif Jawab_KetemuReruntuhan == JawabD :
        print("Kamu Memutuskan Untuk Membangun Tenda")
        print("Namun Kamu Tidak Bisa Tidur")
        print("Pikiranmu Terus Terpusat Pada Reruntuhan Itu")
        print("Pada Akhirnya Kamu Memutuskan Untuk Memasuki Reruntuhan Itu")
        print("Seketika Setelah Kamu Masuk, Pintu Reruntuhan Tersebut Mulai Runtuh")
        EnterLanjut_1()
    else :
        print('Coba Lagi')
        KetemuReruntuhan()
def EnterLanjut_1():
    EnterLanjut1 = input ('Tekan ENTER untuk lanjut')
    MasukReruntuhan()
def MasukReruntuhan():
    print("Kamu Memutuskan Untuk Melihat Kembali Pintu Masuk Yang Telah Runtuh Tadi")
    print("Reruntuhan Itu Jatuh Sempurna Menutupi Pintu Masuk")
    print('"Tak Bisa Dilewati" Pikirmu')
    print("Kamu Memperhatikan Nilai Statusmu")
    print("Kesehatan")
    print(Kesehatan)
    print("Stamina")
    print(Stamina)
    print("Haus")
    print(Haus)
    print("Lapar")
    print(Lapar)
    EnterLanjut_2()
def EnterLanjut_2():
    EnterLanjut2 = input ('Tekan ENTER untuk lanjut')
    MasukReruntuhan2()
def MasukReruntuhan2():
    print("Kamu melihat kondisi ruangan di sekitaarmu")
    print("Kamu melihat beberapa jalan")
    print("Satu diantaranya menuju ke ruangan bawah")
    print("Satu diantaranya menuju ke sebuah ruangan yang masih tampak bagus")
    print("Satu diantaranya menuju ke perpustakaan tua")
    print("Satunya lagi menuju ke semacam gudang")
    print("Kemanakah kamu akan pergi")
    print("A. Ruangan Bawah")
    print("B. Ruangan Yang Masih Bagus")
    print("C. Perpustakaan Tua")
    print("D. Gudang Tua")
    JawabMasukReruntuhan()
def JawabMasukReruntuhan()
    Jawab_MasukReruntuhan_1 = input ("Jawab : ")
    if Jawab_MasukReruntuhan_1 == JawabA :
        Reruntuhan_RuangBawah_Masuk()
    elif Jawab_MasukReruntuhan_1 == JawabB :
        Reruntuhan_RuangBagus_Masuk()
    elif Jawab_MasukReruntuhan_1 == JawabC :
        Reruntuhan_PerpusTua_Masuk()
    elif Jawab_MasukReruntuhan_1 == JawabD :
        Reruntuhan_GudangTua_Masuk()
    else:
        JawabMasukReruntuhan()
def Reruntuhan_RuangBawah_Masuk():
    print ("Kamu mulai berjalan ke ruangan tersebut")
    print ("Ruangan tersebut nampak berantakan")
    print ("Kamu mulai melihat-lihat sekitar")
    print ("Kamu melihat dua buah pintu di sisi yang saling berlawanan")
    print ("Kemana kamu akan pergi?")
    print ("A. Kiri")
    print ("B. Kanan")
    Reruntuhan_RuangBawah_Masuk_Jawab()
def Reruntuhan_RuangBagus_Masuk():
    print('Kamu Membuka pintu ruangan')
    print('Kamu melihat sekitar dan ruangan itu tampak lumayan panjang')
    print('"Tempat ini lebih seperti lorong" Pikirmu')
    print('Selain itu ruangan tersebut tidak terlalu gelap')
    print('Terdapat semacam lentera yang sangat antik berjejer dengan rapi')
    print('Dalam lentera tersebut tepancar api biru yang tidak masuk akal')
    print('Kamu diam sejenak dan Memutuskan untuk masuk ke ruangan tersebut')
    print('Kamu segera masuk dan menutup pintu tempat kamu tadi')
    print('Apakah kamu ingin mengunci pintu tersebut?')
    Reruntuhan_RuangBagus_Pintu()
def Reruntuhan_PerpusTua_Masuk():
    print('Kamu membuka pintu perlahan')
    print('Perpustakan tua tersebut sudah sangat tua dan berdebu')
    print('Kamu berjalan kedalam ruangan')
    print('Kamu tidak sengaja menyenggol sebuah barang hingga barang tersebut jatuh ke karpet di bawahnya')
    print('Kamu mengambil barang tersebut dan mengamatinya')
    print('Kamu menemukan lentera')
    print('Kamu menyalakan lentera tersebut menggunakan korek api di sakumu')
    print('Lentera tersebut bersinar dengan terang')
    print('Kamu mulai melihat ke sekitar dan menemukan bahwa ruangan tersebut sangat besar')
    Reruntuhan_PerpusTua_Masuk_PencetLanjut_1 = input ('Tekan ENTER untuk lanjut')
    print('Kamu mulai berjalan ke rak terdekat')
    print('Kamu mendengar suara keras dari bawahmu')
    print('Suaranya seperti ada gerobak yang meluncur dengan cepat dan menabrak gubug')
    print('Keringat menetes dari dahimu')
    print('Kamu melihat kembali pintu tempatmu masuk masih terbuka')
    print('Apa yang ingin kamu lakukan?')
    print('A. Tutup pintunya')
    print('B. Tutup dan Kunci Pintunya')
    print('C. Biarkan Terbuka')
    Reruntuhan_PerpusTua_Masuk_2()
def Reruntuhan_PerpusTua_Masuk_2():
    global PoinBeruang
    Reruntuhan_PerpusTua_PintuMasuk = input ('Jawab : ')
    if Reruntuhan_PerpusTua_PintuMasuk == JawabA :
        print('Kamu memutuskan untuk menutup pintu masuk tadi')
        print('Setelah itu kembali menuju rak tadi')
    elif Reruntuhan_PerpusTua_PintuMasuk == JawabB :
        PoinBeruang -= 1
        print('Kamu memutuskan untuk menutup dan mengunci pintu masuk tadi')
        print('Kamu mulai berjalan mundur perlahan untuk beberapa langkah')
        print('Kemudian kamu kembali menuju rak tadi')
    elif Reruntuhan_PerpusTua_PintuMasuk == JawabC :
        PoinBeruang += 1
        print('Kamu memutuskan untuk membiarkan pintu masuk terbuka')
        print('Kamu kembali melihat buku-buku yang ada di rak tersebut')
    else:
        Reruntuhan_PerpusTua_Masuk_2()
def Reruntuhan_GudangTua_Masuk():
    print('Kamu berjalan ke sebuah ruangan yang nampak seperti gudang')
    print('Di dalam ruangan tersebut tampak beberapa rak dan terdapat pula beberapa pintu')
    print('')
'''
Gameplay Part 1, Selesai
'''
#---------------------
'''
Gameplay Part 2, Mulai
'''
'''
Gameplay Part 2, Selesai
'''
#---------------------
'''
Gameplay Part 3, Mulai
'''
'''
Gameplay Part 3, Selesai
'''
#---------------------
'''
Eksekusi Menu Awal, Mulai
'''
StartMenu1()
StartMenu2()
'''
Eksekusi Menu Awal, Selesai
'''
#---------------------
'''
Eksekusi Gameplay, Mulai
'''

'''
Eksekusi Gameplay, Selesai
'''
#---------------------
