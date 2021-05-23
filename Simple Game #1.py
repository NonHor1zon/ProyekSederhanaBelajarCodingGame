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
JawabA = "A" or "a"
JawabB = "B" or "b"
JawabC = "C" or "c"
JawabD = "D" or "d"
JawabYa = "Ya" or "ya" or "YA"
JawabTidak = "Tidak" or "tidak" or "TIDAK"
JawabKiri = "Kiri" or "kiri" or "KIRI"
JawabKanan = "Kanan" or "kanan" or "KANAN"
JawabAtas = "Atas" or "atas" or "ATAS"
JawabBawah = "Bawah" or "bawah" or "BAWAH"
JawabLakukan = "Lakukan" or "lakukan" or "LAKUKAN"
JawabJangan = "Jangan" or "jangan" or "JANGAN"
JawabSetuju = "Setuju" or "setuju" or "SETUJU"
JawabTolak = "Tolak" or "tolak" or "TOLAK"
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
KoinAntik = 0
Pintu_RuangBagus1 = 0
Senter = 0
Cahaya = 0
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
    global Cahaya
    print('Kamu Membuka pintu ruangan')
    print('Kamu melihat sekitar dan ruangan itu tampak lumayan panjang')
    print('"Tempat ini lebih seperti lorong" Pikirmu')
    print('Selain itu ruangan tersebut tidak terlalu gelap')
    print('Terdapat semacam lentera yang sangat antik berjejer dengan rapi')
    print('Dalam lentera tersebut tepancar api biru yang tidak masuk akal')
    Cahaya += 2
    print('Kamu diam sejenak dan Memutuskan untuk masuk ke ruangan tersebut')
    print('Kamu segera masuk dan menutup pintu tempat kamu tadi')
    print('Apakah kamu ingin mengunci pintu tersebut?')
    print('Ya / Tidak')
    Reruntuhan_RuangBagus_Pintu()
def Reruntuhan_RuangBagus_Pintu():
    global Pintu_RuangBagus1
    Reruntuhan_RuangBagus_Pintu1_Kunci = input ('Jawab : ')
    if Reruntuhan_RuangBagus_Pintu1_Kunci == JawabYa :
        Pintu_RuangBagus1 += 1
        print('Kamu memutuskan untuk mengunci pintu tersebut')
        print('Kamu memasukkan kunci pintu itu kedalam kantongmu')
        print('Kamu mulai berjalan menuju dalam ruangan')
        Reruntuhan_RuangBagus_Lorong()
    elif Reruntuhan_RuangBagus_Pintu1_Kunci == JawabTidak :
        print ('Kamu memutuskan untuk tidak mengunci pintu tersebut')
        print ('Kamu kembali melihat ke arah lorong tersebut')
        print ('Kamu mulai berjalan ke arah lorong tersebut')
        Reruntuhan_RuangBagus_Lorong()
    else:
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
    print('Kamu melihat barang-barang yang ada di rak tersebut')
    print('Kamu melihat koin tua')
    print('Apakah kamu ingin mengambil koin tua tersebut?')
    print('A. Ambil')
    print('B. Tidak')
    Reruntuhan_GudangTua_KoinAntik()
def Reruntuhan_GudangTua_KoinAntik(): 
    global KoinAntik
    Reruntuhan_GudangTua_KoinAntik_Ambil = input ('Jawab : ')
    if Reruntuhan_GudangTua_KoinAntik_Ambil == JawabA :
        print('Kamu memutuskan untuk mengambil koin antik tadi')
        KoinAntik += 1
        print('Koin Antik + 1')
        EnterLanjut_GudangTua_Ruang1()
    elif Reruntuhan_GudangTua_KoinAntik_Ambil == JawabB :
        print('Kamu memutuskan untuk meninggalkan koin antik tadi')
        print('Kamu kembali menelusuri ruangan')
        EnterLanjut_GudangTua_Ruang1()
    else:
        Reruntuhan_GudangTua_KoinAntik_Ambil1()
def EnterLanjut_GudangTua_Ruang1():
    EnterLanjut_GudangTuaRuang1 = input ('Tekan ENTER untuk lanjut')
    Reruntuhan_GudangTua_Masuk2()
'''
Gameplay Part 1, Selesai
'''
#---------------------
'''
Gameplay Part 2, Mulai
'''
def Reruntuhan_RuangBawah_Masuk_Jawab():
    Reruntuhan_RuangBawah_Masuk_Jawaban = input('Jawab : ')
    if Reruntuhan_RuangBawah_Masuk_Jawaban == JawabKiri :
        print('Kamu memilih untuk pergi ke ruangan kiri')
        Reruntuhan_RuangBawah_Kiri_Masuk()
    if Reruntuhan_RuangBawah_Masuk_Jawaban == JawabKanan :
        print('Kamu memilih untuk pergi ke ruangan kanan')
        Reruntuhan_RuangBawah_Kanan_Masuk()
    else:
        Reruntuhan_RuangBawah_Masuk_Jawab()
def Reruntuhan_RuangBawah_Kiri_Masuk():
    print('Kamu membuka pintu sebelah kiri')
    print('Pintu tersebut terasa lumayan berat')
    print('Kamu tetap berusaha, hingga pintu tersebut terbuka')
    print('Kamu menemukan selembar perkamen tua yang sudah agak buram')
    print('Perkamen tersebut dibuat dari bahasa yang tidak kamu ketahui')
    print('Kamu mulai kembali melihat sekeliling')
    print('Kamu menemukan senter')
    print('Apakah kamu ingin mencoba menyalakannya?')
    print('Ya / Tidak')
def Reruntuhan_RuangBawah_Kiri_Senter():
    global Senter
    global Cahaya
    global Stamina
    Reruntuhan_RuangBawah_Kiri_NyalaSenter = input ('Jawab : ')
    if Reruntuhan_RuangBawah_Kiri_NyalaSenter == JawabYa :
        print('Kamu mencoba menyalakan senter tersebut')
        print('Kamu mulai mencari baterai di ruangan tersebut')
        print('Stamina -10')
        Stamina -= 10
        Senter += 1
        Cahaya += 1
        print('Kamu berdiri di depan sebuah rak tua')
        print('Kamu mengambil baterai dimeja dan memasangkannya ke senter')
        Reruntuhan_RuangBawah_Kiri_PetiKecil()
    elif Reruntuhan_RuangBawah_Kiri_NyalaSenter == JawabTidak :
        print('Kamu memasukkan senter tersebut kedalam tas')
        Senter += 1
        print('Kamu terus menjelajahi ruangan itu dalam gelap')
        Reruntuhan_RuangBawah_Kiri_PetiKecil()
    else :
        Reruntuhan_RuangBawah_Kiri_Senter()

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
