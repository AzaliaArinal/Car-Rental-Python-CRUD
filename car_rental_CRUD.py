# BISMILLAH
# /==========  CAPSTONE PROJECT    ==========/
# /========== AZALIA ANANDA ARINAL ==========/
# /==========     RENTAL MOBIL     ==========/

from datetime import datetime

# /==================== DATA ====================/
userpass = {
   'admin' : 'admin'
}

tabel_mobil = [
   {
      'no_polisi' : 'L 1 A',
      'Merek' : 'FIAT  ',
      'Tipe' :'FIAT 500',
      'Transmisi' : 'MT',
      'Harga' : 500000,
      'status' : 'TERSEDIA'
   },
   {
      'no_polisi' : 'L 21 C',
      'Merek' : 'TESLA',
      'Tipe' :'CYBERTRUCK',
      'Transmisi' : 'AT',
      'Harga' : 1000000,
      'status' : 'TERSEDIA'
   },
   {
      'no_polisi' : 'L 98 E',
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

tabel_transaksi= []

# /==================== VALIDATION ====================/
def validate_car_id(plate_numb):
   for i in tabel_mobil:
      if i['no_polisi'] == plate_numb:
         return i
   return None



def validate_customer_id(customer_id):
   for i in tabel_customer:
      if i['customer_id'] == customer_id:
         return True
   return False



def validate_rent_id(rent_id):
   for transaction in tabel_transaksi:
      if transaction['rent_id'] == rent_id:
         return transaction
   return None



def validate_date(input_date):
   try:
      datetime.strptime(input_date, '%Y-%m-%d')
      return True
   except ValueError:
      return False



# /==================== READ ====================/

def cari_customer(cari_nama_cust):
    hasil_cari_nama = [i for i in tabel_customer if i['Nama'].lower() == cari_nama_cust.lower()]
    if not hasil_cari_nama:
        print("DATA CUSTOMER TIDAK DITEMUKAN:", cari_nama_cust)
    else:
        print('ID\t| Nama Customer \t| Alamat \t| No. HP \t\t| No. KTP \t| No. SIM|')
        for i in hasil_cari_nama:
            print(f'{i['customer_id']} \t| {i['Nama']} \t| {i['Alamat']} \t| {i['no_hp']}\t\t| {i['no_KTP']} \t| {i['no_SIM']}|')




def cari_mobil(cari_no_polisi):
    hasil_cari = [i for i in tabel_mobil if i['no_polisi'].lower() == cari_no_polisi.lower()]
    if not hasil_cari:
        print("DATA MOBIL TIDAK DITEMUKAN:", cari_no_polisi)
    else:
        print('No.Polisi \t| Merek \t| Tipe \t\t| Transmisi \t| Harga \t| Status  |')
        for i in hasil_cari:
            print(f'{i['no_polisi']} \t| {i['Merek']} \t| {i['Tipe']} \t| {i['Transmisi']}\t\t| {i['Harga']} \t| {i['status']}|')






# /==================== UPDATE ====================/

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
        if i['no_polisi'] == id_mobil:
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




# /==================== TRANSACTION ====================/
def rent_transaction():
   rent_id = input("Enter new rent ID: ")

   # input plate number
   while True:
      plate_numb = input("Enter car's plate number: ")
      i = validate_car_id(plate_numb)
      if i and i['status'] == 'TERSEDIA':
         break
      else:
         print("Car ID or car is not available. Try again")
   
   # input customer ID
   while True:
      customer_id = input("Enter customer ID: ")
      if validate_customer_id(customer_id):
         break
      else:
         print("Invalid customer ID. Try again")
   
   # input start and end date
   while True:
      start_date = input("Enter start rent date (YYYY-MM-DD): ")
      if validate_date(start_date):
         start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
         break
      else:
         print("Invalid date format. Try again")
   
   while True:
      end_date = input("Enter start rent date (YYYY-MM-DD): ")
      if validate_date(end_date):
         end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
         if end_date >= start_date:
            break
         else:
            print("End date must be greater than Start date. Try again")
      else:
         print("Invadil date format. Try again")
   

   # count rental days and total amount
   rental_days = (end_date - start_date).days + 1
   total_amount = rental_days * i['Harga']

   confirm_rent = input("Submit transaction? Y/N: ")
   if confirm_rent == 'Y' or 'y':
      i['status'] = 'NOT AVAILABLE'

      transaction = {
         'rent_id' : rent_id,
         'plate_number' : plate_numb,
         'customer_id' : customer_id,
         'start_rent_count' : start_date.isoformat(),
         'end_rent_count' : end_date.isoformat(),
         'rent_days_count' : rental_days,
         'total' : total_amount,
         'late_fee' : 0
      }
      tabel_transaksi.append(transaction)
      print("Rent transaction added")
   else:
      print("Cancel transaction")




late_fee = 200000

def calculate_late_fee(late_days, daily_rent):
    daily_penalty = daily_rent * 0.1  # Assuming 10% of the daily rent as the penalty per day
    return late_days * daily_penalty

def return_transaction():
   while True:
      rent_id = input("Enter rent transaction ID: ")
      transaction = validate_rent_id(rent_id)
      if transaction:
         break
      else:
         print("Invalid transaction ID. Try again")
   

   while True:
      return_date = input("Enter return date (YYYY-MM-DD): ")
      if validate_date(return_date):
         return_date = datetime.strptime(return_date, '%Y-%m-%d').date()
         break
      else:
         print("Invalid date format. Try again")


   late_fee_count = 0
   late_return_date = input("Enter late return date (YYYY-MM-DD), Enter to skip: ").strip()
   if late_return_date:
      while True:
         if validate_date(late_return_date):
            late_return_date = datetime.strptime(late_return_date, '%Y-%m-%d').date()
            break
         else:
            print("Invadil date format. Try again")

         if late_return_date > return_date:
            late_days = (late_return_date - return_date).days
            late_fee_count = late_days * late_fee

   confirm_return = input("Submit transaction? Y/N: ")
   if confirm_return == 'Y' or 'y':
      transaction['late_fee'] = late_fee_count

      car = validate_car_id(transaction['plate_number'])
      car['status'] = 'AVAILABLE'

      print ("Return transaction added")
   else:
      print("Cancel transaction")
   
   
   
   
# /==================== SHOW TABLES ====================/
def show_transaction_table():
   if len(tabel_transaksi) == 0:
      print("\nThere is no transaction data\n")
   else:
      print("==========TABEL DATA CUSTOMER==========\n")
      print('|Rent ID\t| Plate Number \t| Customer ID \t| Start Date \t| End Date \t| Days  | Late Fee | Total Amount')
      for i in range(len(tabel_transaksi)):
         print(f'| {tabel_transaksi[i]['rent_id']} \t| {tabel_transaksi[i]['plate_number']} \t| {tabel_transaksi[i]['customer_id']} \t| {tabel_transaksi[i]['start_rent_count']}\t| {tabel_transaksi[i]['end_rent_count']}\t| {tabel_transaksi[i]['rent_days_count']}\t| {tabel_transaksi[i]['late_fee']}\t\t| {tabel_transaksi[i]['total']}')





# /==================== MENU ====================/
def menu():
   while True:
      print("==========MENU UTAMA==========")
      print("1. TRANSAKSI")
      print("2. DATA CUSTOMER")
      print("3. DATA MOBIL")
      print("4. LOGOUT")
      pilihan_menu = input("MASUKKAN PILIHAN MENU: ")
      if pilihan_menu == '1':
         transaksi()
      elif pilihan_menu == '2':
         data_customer()
      elif pilihan_menu == '3':
         data_mobil()
      elif pilihan_menu == '4':
         print("LOGGING OUT")
         exit()
      else:
         print("MASUKKAN PILIHAN LAGI")





def transaksi():
   while True:
      print("\n==========MENU TRANSAKSI==========")
      print("1. BUAT TRANSAKSI PINJAM")
      print("2. BUAT TRANSAKSI KEMBALI")
      print("0. BACK TO MAIN MENU")

      show_transaction_table()

      pilihan_transaksi = input("MASUKKAN PILIHAN MENU: ")
            
      if pilihan_transaksi == '1':
         print("\n==========TRANSAKSI PINJAM==========")
         rent_transaction()
      
      
      if pilihan_transaksi == '2':
         print("\n==========TRANSAKSI KEMBALI==========")
         return_transaction()
      
      elif pilihan_transaksi == '0':
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
      print(f'|{i} \t| {tabel_mobil[i]['no_polisi']} \t| {tabel_mobil[i]['Merek']} \t| {tabel_mobil[i]['Tipe']} \t| {tabel_mobil[i]['Transmisi']}\t\t| {tabel_mobil[i]['Harga']} \t| {tabel_mobil[i]['status']}|')
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
            'no_polisi' : no_polisi,
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

if __name__ == "__main__":
   menu()