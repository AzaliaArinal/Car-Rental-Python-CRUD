# BISMILLAH
# /==========  CAPSTONE PROJECT    ==========/
# /========== AZALIA ANANDA ARINAL ==========/
# /==========     RENTAL MOBIL     ==========/

# DATA
userpass = {
   'admin' : 'admin'
}

tabel_mobil = [
   {
      'No_polisi' : 'L 1 A',
      'Merek' : 'FIAT  ',
      'Tipe' :'FIAT 500',
      'Transmisi' : 'MT',
      'Harga' : 500000,
      'status' : 'TERSEDIA'
   },
   {
      'No_polisi' : 'L 21 C',
      'Merek' : 'TESLA',
      'Tipe' :'CYBERTRUCK',
      'Transmisi' : 'AT',
      'Harga' : 1000000,
      'status' : 'TERSEDIA'
   },
   {
      'No_polisi' : 'L 98 E',
      'Merek' : 'PEUGEOT',
      'Tipe' :'205 GTI',
      'Transmisi' : 'MT',
      'Harga' : 750000,
      'status' : 'TERSEDIA'
   }
]

tabel_customer = [
   {
      'customer_id' : 'CT0001',
      'Nama' : 'MISS ANYA FORGER',
      'Alamat' : 'SURABAYA',
      'no_hp' : 6282188080698,
      'no_KTP' : 123456778,
      'no_SIM' : 101010
   },
   {
      'customer_id' : 'CT0002',
      'Nama' : 'TAKI TACHIBANA',
      'Alamat' : 'MANADO',
      'no_hp' : 6282291173144,
      'no_KTP' : 123456788,
      'no_SIM' : 202020
   },
   {
      'customer_id' : 'CT0003',
      'Nama' : 'NICHOLAS SAPUTRA',
      'Alamat' : 'TANGKAHAN',
      'no_hp' : 6282122911742,
      'no_KTP' : 122345678,
      'no_SIM' : 303030
   }
]

tabel_pinjam = [
   {
      'id_pinjam' : 'P-0001',
      'nama_cust' : 'MISS ANYA FORGER',
      'no_polisi' : 'L 21 C',
      'tanggal_pinjam' : '2024-02-21',
      'tanggal_kembali' : '2024-02-27',
      'lama_sewa' : 7,
      'total' : 7000000,
      'pembayaran' : 'Cash'
   }
]

tabel_kembali = [
   {
      'id_pinjam' : 'P-0001',
      'nama_cust' : 'MISS ANYA FORGER',
      'no_polisi' : 'L 21 C',
      'tanggal_pinjam' : '2024-02-21',
      'tanggal_kembali' : '2024-02-27',
      'lama_sewa' : 7,
      'lama_denda' : 3,
      'total' : 7000000,
      'pembayaran' : 'Cash'
   }
]

def cari_mobil(cari_no_polisi):
    hasil_cari = [i for i in tabel_mobil if i['No_polisi'].lower() == cari_no_polisi.lower()]
    if not hasil_cari:
        print("DATA MOBIL TIDAK DITEMUKAN:", cari_no_polisi)
    else:
        print('No.Polisi \t| Merek \t| Tipe \t\t| Transmisi \t| Harga \t| Status  |')
        for i in hasil_cari:
            print(f'{i['No_polisi']} \t| {i['Merek']} \t| {i['Tipe']} \t| {i['Transmisi']}\t\t| {i['Harga']} \t| {i['status']}|')



def cari_customer(cari_nama_cust):
    hasil_cari_nama = [i for i in tabel_customer if i['Nama'].lower() == cari_nama_cust.lower()]
    if not hasil_cari_nama:
        print("DATA CUSTOMER TIDAK DITEMUKAN:", cari_nama_cust)
    else:
        print('ID\t| Nama Customer \t| Alamat \t| No. HP \t\t| No. KTP \t| No. SIM|')
        for i in hasil_cari_nama:
            print(f'{i['customer_id']} \t| {i['Nama']} \t| {i['Alamat']} \t| {i['no_hp']}\t\t| {i['no_KTP']} \t| {i['no_SIM']}|')



def update_customer(id_cust, nama_baru=None, alamat_baru=None, hp_baru=None, ktp_baru=None, sim_baru=None):
    for i in tabel_customer:
        if i['customer_id'] == id_cust:
            if nama_baru:
                i['Nama'] = nama_baru
            if alamat_baru:
                i['Alamat'] = alamat_baru
            if hp_baru:
                i['no_hp'] = hp_baru
            if ktp_baru:
               i['no_KTP'] = ktp_baru
            if sim_baru:
                i['no_SIM'] = sim_baru
            print("DATA CUSTOMER BERHASIL DIUPDATE")
            return
    print("CUSTOMER TIDAK DITEMUKAN")



def update_mobil(id_mobil, merek_baru=None, tipe_baru=None, transmisi_baru=None, harga_baru=None, status_baru=None):
    for i in tabel_mobil:
        if i['No_polisi'] == id_mobil:
            if merek_baru:
                i['Merek'] = merek_baru
            if tipe_baru:
                i['Tipe'] = tipe_baru
            if transmisi_baru:
                i['Transmisi'] = transmisi_baru
            if harga_baru:
               i['Harga'] = harga_baru
            if status_baru:
                i['status'] = status_baru
            print("DATA MOBIL BERHASIL DIUPDATE")
            return
    print("MOBIL TIDAK DITEMUKAN")
   



def menu():
   while True:
      print("==========MENU UTAMA==========")
      print("1. PINJAM MOBIL")
      print("2. PENGEMBALIAN MOBIL")
      print("3. DATA CUSTOMER")
      print("4. DATA MOBIL")
      print("5. LOGOUT")
      pilihan_menu = input("MASUKKAN PILIHAN MENU: ")
      if pilihan_menu == '1':
         pinjam_mobil()
      elif pilihan_menu == '2':
         pengembalian_mobil()
      elif pilihan_menu == '3':
         data_customer()
      elif pilihan_menu == '4':
         data_mobil()
      elif pilihan_menu == '5':
         print("LOGGING OUT")
         exit()
      else:
         print("MASUKKAN PILIHAN LAGI")





def pinjam_mobil():
   # while True:
      print("==========MENU PINJAM MOBIL==========")
      print("1. BUAT TRANSAKSI BARU")
      print("0. BACK TO MAIN MENU")
      print("TABEL DATA CUSTOMER\n")
      print('|ID Pinjam\t| NamaCust \t\t\t| Tanggal Pinjam \t| Tanggal Kembali \t\t| Lama sewa \t| Pembayaran|')
      for i in range(len(tabel_pinjam)):
         print(f'| {tabel_pinjam[i]['id_pinjam']} \t| {tabel_pinjam[i]['nama_cust']} \t| {tabel_pinjam[i]['no_polisi']} \t| {tabel_pinjam[i]['tanggal_pinjam']}\t| {tabel_pinjam[i]['tanggal_kembali']} | {tabel_pinjam[i]['lama_sewa']}\t| {tabel_pinjam[i]['total']}\t| {tabel_pinjam[i]['pembayaran']}\t|')
      pilihan_pinjam = input("MASUKKAN PILIHAN MENU: ")
      if pilihan_pinjam == '1':
         konfirmasi = input("BUAT TRANSAKSI PINJAM? Y/N: ")
         if konfirmasi == 'Y' or 'y':
            # start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            # end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            # rental_days = (end_date_obj - start_date_obj).days + 1
            # total_amount = rental_days * daily_rental_rate
            print("TRANSAKSI BERHASIL DIBUAT")
            # pinjam_mobil()
         elif konfirmasi == 'N' or 'n':
            # pinjam_mobil()
            print("KEMBALI KE MENU PINJAM MOBIL")
         else:
            print("MASUKKAN PILIHAN LAGI")
      elif pilihan_pinjam == '0':
         menu()
      else:
         print("MASUKKAN PILIHAN LAGI")





def pengembalian_mobil():
   # while True:
      print("==========MENU PENGEMBALIAN MOBIL==========")
      print("1. BUAT TRANSAKSI BARU")
      print("0. BACK TO MAIN MENU")
      print("tabel TRANSAKSI PINJAM")
      for i in range(len(tabel_kembali)):
         print(f'| {tabel_kembali[i]['id_pinjam']} \t| {tabel_kembali[i]['nama_cust']} \t| {tabel_kembali[i]['no_polisi']} \t| {tabel_kembali[i]['tanggal_pinjam']}\t| {tabel_kembali[i]['tanggal_kembali']} | {tabel_kembali[i]['lama_sewa']}\t| {tabel_kembali[i]['lama_denda']}\t| {tabel_kembali[i]['total']}\t| {tabel_kembali[i]['pembayaran']}\t|')
      pilihan_kembali = input("MASUKKAN PILIHAN MENU: ")
      if pilihan_kembali == '1':
         konfirmasi_kembali = input("BUAT TRANSAKSI PENGEMBALIAN MOBIL? Y/N: ")
         if konfirmasi_kembali == 'Y' or 'y':
            print("TRANSAKSI BERHASIL DIBUAT")
         elif konfirmasi_kembali == 'N' or 'n':
            print("KEMBALI KE MENU UTAMA")
         else:
            print("MASUKKAN PILIHAN LAGI")
      elif pilihan_kembali == '0':
         menu()
      else:
         print("MASUKKAN PILIHAN LAGI")




def data_customer():
   print("==========MENU DATA CUSTOMER==========")
   print("1. BUAT DATA CUSTOMER BARU")
   print("2. CARI CUSTOMER")
   print("3. EDIT DATA CUSTOMER")
   print("4. DELETE DATA CUSTOMER")
   print("0. BACK TO MAIN MENU")
   print("==========TABEL DATA CUSTOMER==========\n")
   print('|Index\t| ID Customer \t| Nama Customer \t| Alamat \t| No. HP \t\t| No. KTP \t| No. SIM|')
   for i in range(len(tabel_customer)):
      print(f'|{i} \t| {tabel_customer[i]['customer_id']} \t| {tabel_customer[i]['Nama']} \t| {tabel_customer[i]['Alamat']} \t| {tabel_customer[i]['no_hp']} \t| {tabel_customer[i]['no_KTP']}\t| {tabel_customer[i]['no_SIM']} |')
   pilihan_4 = input("MASUKKAN PILIHAN MENU: ")
   
   
   if pilihan_4 == '1':
      print("==========BUAT DATA CUSTOMER BARU==========")
      id_cust = input("ID CUSTOMER: ")
      nama_cust = input("NAMA CUSTOMER: ")
      alamat = input("ALAMAT: ")
      no_hp = input("NO. HP: ")
      no_ktp = input("NO. KTP: ")
      no_sim = input("NO. SIM: ")
      konfirmasi_4 = input("SUBMIT? Y/N: ")
      if konfirmasi_4 == 'Y' or 'y':
         tabel_customer.append({
            'customer_id' : id_cust,
            'Nama' : nama_cust,
            'Alamat' : alamat,
            'no_hp' : no_hp,
            'no_KTP' : no_ktp,
            'no_SIM' : no_sim
         })
         print("DATA BERHASIL DIINPUT")
      elif konfirmasi_4 == 'N' or 'n':
         print("KEMBALI KE MENU UTAMA")
      else:
         print("MASUKKAN PILIHAN LAGI")
   
   
   elif pilihan_4 == '2':
      print("==========CARI DATA CUSTOMER==========")
      # print('''CARI BERDASARKAN: 
      #    ID CUSTOMER/NAMA
      #    ''')
      # print("MASUKKAN ID CUSTOMER: ")
      cari_nama_cust = input("MASUKKAN NAMA CUSTOMER: ")
      cari_customer(cari_nama_cust)
      # konfirmasi_4 = input("CARI LAGI? Y/N: ")
      # if konfirmasi_4 == 'Y' or 'y':
      #    print("TRANSAKSI BERHASIL")
      # elif konfirmasi_4 == 'N' or 'n':
      #    print("KEMBALI KE MENU UTAMA")
      # else:
      #    print("MASUKKAN PILIHAN LAGI")
   
   
   elif pilihan_4 == '3':
      print("==========UBAH DATA CUSTOMER==========")
      id_cust = input("MASUKKAN ID CUSTOMER: ")
      nama_baru = input("MASUKKAN NAMA BARU: ")
      alamat_baru = input("MASUKKAN ALAMAT BARU: ")
      hp_baru = input("MASUKKAN NO. HP BARU: ")
      ktp_baru = input("MASUKKAN NO. KTP BARU: ")
      sim_baru = input("MASUKKAN NO. SIM BARU: ")
      konfirmasi_4 = input("EDIT DATA CUSTOMER? Y/N: ")
      if konfirmasi_4 == 'Y' or 'y':
         update_customer(id_cust, nama_baru or None, alamat_baru or None, hp_baru or None, ktp_baru or None, sim_baru or None)
      elif konfirmasi_4 == 'N' or 'n':
         print("KEMBALI KE MENU UTAMA")
      else:
         print("MASUKKAN PILIHAN LAGI")
   
   
   elif pilihan_4 == '4':
      print("==========HAPUS DATA CUSTOMER==========")
      index_cust = int(input("MASUKKAN INDEX CUSTOMER: "))
      konfirmasi_4 = (input(f"HAPUS DATA CUSTOMER {index_cust}? Y/N: "))
      if konfirmasi_4 == 'Y' or 'y':
         del tabel_customer[index_cust]
         print("TRANSAKSI BERHASIL")
      elif konfirmasi_4 == 'N' or 'n':
         print("KEMBALI KE MENU UTAMA")
      else:
         print("MASUKKAN PILIHAN LAGI")
   
   
   elif pilihan_4 == '0':
      menu()
   else:
      print("MASUKKAN PILIHAN LAGI")





def data_mobil():
   print("==========MENU DATA MOBIL==========")
   print("1. TAMBAH DATA MOBIL")
   print("2. CARI DATA MOBIL")
   print("3. EDIT DATA MOBIL")
   print("4. HAPUS DATA MOBIL")
   print("0. BACK TO MAIN MENU")
   print("TABEL DATA MOBIL\n")
   print('|Index\t| No.Polisi \t| Merek \t| Tipe \t\t| Transmisi \t| Harga \t| Status  |')
   for i in range(len(tabel_mobil)):
      print(f'|{i} \t| {tabel_mobil[i]['No_polisi']} \t| {tabel_mobil[i]['Merek']} \t| {tabel_mobil[i]['Tipe']} \t| {tabel_mobil[i]['Transmisi']}\t\t| {tabel_mobil[i]['Harga']} \t| {tabel_mobil[i]['status']}|')
   pilihan_5 = input("MASUKKAN PILIHAN MENU: ")
   
   
   if pilihan_5 == '1':
      print("==========BUAT DATA MOBIL BARU==========")
      no_polisi = input("NO. POLISI: ")
      merek = input("MASUKKAN MEREK MOBIL: ")
      tipe = input("MASUKKAN TIPE MOBIL: ")
      transmisi = input("MASUKKAN TRANSMISI: ")
      harga = input("MASUKKAN HARGA SEWA: ")
      status = input("MASUKKAN KETERSEDIAAN MOBIL: ")
      konfirmasi_5 = input("SUBMIT? Y/N: ")
      if konfirmasi_5 == 'Y' or 'y':
         tabel_mobil.append({
            'No_polisi' : no_polisi,
            'Merek' : merek,
            'Tipe' : tipe,
            'Transmisi' : transmisi,
            'Harga' : harga,
            'status' : status
         })
         print("DATA BERHASIL DIINPUT")
      elif konfirmasi_5 == 'N' or 'n':
         print("KEMBALI KE MENU UTAMA")
      else:
         print("MASUKKAN PILIHAN LAGI")


   elif pilihan_5 == '2':
      print("==========CARI DATA MOBIL==========")
      # print('''CARI BERDASARKAN: 
      #    ID/MEREK/TIPE/PLAT/TRANSMISI/TAHUN/HARGA/KETERSEDIAAN
      #    ''')
      cari_no_polisi = input("MASUKKAN NO. POLISI: ")
      cari_mobil(cari_no_polisi)
      # konfirmasi_5 = input("CARI LAGI? Y/N: ")
      # if konfirmasi_5 == 'Y' or 'y':
      #    print("TRANSAKSI BERHASIL")
      # elif konfirmasi_5 == 'N' or 'n':
      #    print("KEMBALI KE MENU UTAMA")
      # else:
      #    print("MASUKKAN PILIHAN LAGI")


   elif pilihan_5 == '3':
      print("==========UBAH DATA MOBIL==========")
      id_mobil = input("MASUKKAN NO. POLISI: ")
      merek_baru = input("MASUKKAN MEREK(ENTER JIKA DIKOSONGKAN): ")
      tipe_baru = input("MASUKKAN TIPE BARU: ")
      transmisi_baru = input("MASUKKAN TRANSMISI BARU: ")
      harga_baru = input("MASUKKAN HARGA BARU: ")
      status_baru = input("TERSEDIA/TIDAK TERSEDIA: ")
      konfirmasi_5 = input("EDIT DATA MOBIL? Y/N: ")
      if konfirmasi_5 == 'Y' or 'y':
         update_mobil(id_mobil, merek_baru or None, tipe_baru or None, transmisi_baru or None, harga_baru or None, status_baru or None)
      elif konfirmasi_5 == 'N' or 'n':
         print("KEMBALI KE MENU UTAMA")
      else:
         print("MASUKKAN PILIHAN LAGI")


   elif pilihan_5 == '4':
      print("==========HAPUS DATA MOBIL==========")
      index_mobil = int(input("MASUKKAN INDEX MOBIL: "))
      konfirmasi_5 = (input(f"HAPUS DATA MOBIL {index_mobil}? Y/N: "))
      if konfirmasi_5 == 'Y' or 'y':
         del tabel_mobil[index_mobil]
         print("DATA MOBIL BERHASIL DIHAPUS")
      elif konfirmasi_5 == 'N' or 'n':
         print("KEMBALI KE MENU UTAMA")
      else:
         print("MASUKKAN PILIHAN LAGI")


   elif pilihan_5 == '0':
      menu()
   else:
      print("MASUKKAN PILIHAN LAGI")





# def user_pass(user_pass, username, password):
#    if username in userpass:
#       if userpass[username] == password:
#          return "SUCCESSFUL"
#       else:
#          return "TRY AGAIN"
#    else:
#       return "INVALID INPUT"

# def login():
#    username = input("USERNAME: ")
#    password = input("PASSWORD: ")
#    try_login = user_pass(user_pass, username, password)
#    print(try_login)
#    if try_login == "SUCCESSFUL":
#       menu()

# if __name__ == "__main__":
#    login()

if __name__ == "__main__":
   menu()