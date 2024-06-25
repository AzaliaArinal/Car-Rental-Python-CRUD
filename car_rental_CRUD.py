# BISMILLAH
# /==========  CAPSTONE PROJECT    ==========/
# /========== AZALIA ANANDA ARINAL ==========/
# /==========     RENTAL MOBIL     ==========/

from datetime import datetime

# /==================== DATA ====================/

cars_table = [
   {
      'plate_number' : 'L 1 A',
      'brand' : 'FIAT  ',
      'type' :'FIAT 500',
      'price' : 500000,
      'status' : 'TERSEDIA'
   },
   {
      'plate_number' : 'L 21 C',
      'brand' : 'TESLA',
      'type' :'CYBERTRUCK',
      'price' : 1000000,
      'status' : 'TERSEDIA'
   },
   {
      'plate_number' : 'L 98 E',
      'brand' : 'PEUGEOT',
      'type' :'205 GTI',
      'price' : 750000,
      'status' : 'TERSEDIA'
   }
]

customer_table = [
   {
      'customer_id' : 'CT0001',
      'name' : 'MISS ANYA FORGER',
      'address' : 'SURABAYA',
      'phone' : 6282188080698,
      'KTP' : 123456778,
      'SIM' : 101010
   },
   {
      'customer_id' : 'CT0002',
      'name' : 'TAKI TACHIBANA',
      'address' : 'MANADO',
      'phone' : 6282291173144,
      'KTP' : 123456788,
      'SIM' : 202020
   },
   {
      'customer_id' : 'CT0003',
      'name' : 'NICHOLAS SAPUTRA',
      'address' : 'TANGKAHAN',
      'phone' : 6282122911742,
      'KTP' : 122345678,
      'SIM' : 303030
   }
]

tabel_transaksi= []

# /==================== VALIDATION ====================/
def validate_car_id(plate_numb):
   for i in cars_table:
      if i['plate_number'] == plate_numb:
         return i
   return None



def validate_customer_id(customer_id):
   for i in customer_table:
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



def is_int(value):
   try:
      int(value)
      return True
   except ValueError:
      return False




# /==================== CREATE ====================/

def create_customer(customers):
   while True:
      id_customer = input("Enter ID customer: ")
      if any(customer['customer_id'] == id_customer for customer in customer_table):
         print("ID customer already exists. Please enter a different ID")
         continue

      name = input("Enter Customer name: ")
      address = input("Enter Address: ")
      phone_number = input("Enter Phone number: ")
      if not is_int(phone_number):
            print("Phone number must be an integer. Try again")
            continue
      
      id_card_number = input("Enter ID card number: ")
      if not is_int(id_card_number):
            print("ID card number must be an integer. Try again")
            continue

      drivers_license = input("Enter Driver's license number: ")
      if not is_int(drivers_license):
            print("Driver's license number must be an integer. Try again")
            continue
      
      if any(
            customer['name'] == name and
            customer['address'] == address and
            customer['phone'] == int(phone_number) and
            customer['KTP'] == int(id_card_number) and
            int(customer['SIM']) == int(drivers_license)
            for customer in customer_table
        ):
            print("Customer with the same details already exists.")
            continue
      
      cust_confirm = input("SUBMIT? Y/N: ")
      if cust_confirm == 'Y' or 'y':
         customer_table.append({
            'customer_id' : id_customer,
            'name' : name,
            'address' : address,
            'phone' : phone_number,
            'KTP' : id_card_number,
            'SIM' : drivers_license
         })
         print("Customer added successfully")
         break
      elif cust_confirm == 'N' or 'n':
         print("Back to Main Menu")
         break
      else:
         print("Invalid input")


def create_car(cars):
   while True:
      plate_numb = input("Enter Car's Plate Number: ")
      if any(cars['plate_number'] == plate_numb for cars in cars_table):
         print("Car already exists. Please enter a different number")
         continue

      brand = input("Enter brand: ")
      car_type = input("Enter the type: ")
      car_price = input("Enter rent price per day: ")
      if not is_int(car_price):
            print("Phone number must be an integer. Try again")
            continue
      availability = input("AVAILABLE / NOT AVAILABLE: ")
      if availability not in ['AVAILABLE', 'available', 'NOT AVAILABLE', 'not available']:
         print("Invalid input. Try again")
         continue
      
      if any(
            cars['brand'] == brand and
            cars['type'] == car_type and
            cars['price'] == int(car_price) and
            cars['status'] == availability
            for cars in cars_table
        ):
            print("Car with the same details already exists.")
            continue
      
      confirm_car = input("SUBMIT? Y/N: ")
      if confirm_car == 'Y' or 'y':
         cars_table.append({
            'plate_number' : plate_numb,
            'brand' : brand,
            'type' : car_type,
            'price' : car_price,
            'status' : availability
         })
         print("Car added successfully")
         break
      elif confirm_car == 'N' or 'n':
         print("Back to Main Menu")
         break
      else:
         print("Invalid input")










# /==================== READ ====================/

def search_customer(search_by_ID):
    search_result = [i for i in customer_table if i['name'].lower() == search_by_ID.lower()]
    if not search_result:
        print("Customer not found", search_by_ID)
    else:
      print("| ID Customer \t| Customer Name \t| Address \t| Phone Number \t\t| ID Number \t| Driver's License")
      for i in range(len(customer_table)):
         print(f'| {customer_table[i]['customer_id']} \t| {customer_table[i]['name']} \t| {customer_table[i]['address']} \t| {customer_table[i]['phone']} \t| {customer_table[i]['KTP']}\t| {customer_table[i]['SIM']} |')




def search_car(search_by_plate):
    search_result = [i for i in cars_table if i['plate_number'].lower() == search_by_plate.lower()]
    if not search_result:
        print("Car not found", search_by_plate)
    else:
      print('| Plate Numbers \t| Brand \t| Type \t\t| Price \t| Status  ')
      for i in range(len(cars_table)):
         print(f'| {cars_table[i]['plate_number']} \t| {cars_table[i]['brand']} \t| {cars_table[i]['type']} \t| {cars_table[i]['price']} \t| {cars_table[i]['status']}')






# /==================== UPDATE ====================/

def update_customer(cust_id, new_name=None, new_address=None, new_phone=None, new_IDcard=None, new_license=None):
    for i in customer_table:
        if i['customer_id'] == cust_id:
            if new_name:
                i['name'] = new_name
            if new_address:
                i['address'] = new_address
            if new_phone:
                i['phone'] = new_phone
            if new_IDcard:
               i['KTP'] = new_IDcard
            if new_license:
                i['SIM'] = new_license
            print("Data updated")
            return
    print("Customer not found")

def update_car(plate_numb, new_brand=None, new_type=None, new_price=None, new_status=None):
    for i in cars_table:
        if i['plate_number'] == plate_numb:
            if new_brand:
                i['brand'] = new_brand
            if new_type:
                i['type'] = new_type
            if new_price:
               i['price'] = new_price
            if new_status:
                i['status'] = new_status
            print("Data updated")
            return
    print("Car not found")




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
      end_date = input("Enter end rent date (YYYY-MM-DD): ")
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
   total_amount = rental_days * i['price']

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
      print("========== MAIN MENU ==========")
      print("1. TRANSACTION")
      print("2. CUSTOMER DATA")
      print("3. CAR DATA")
      print("4. LOGOUT")
      choose_menu = input("Your choice: ")
      if choose_menu == '1':
         transaction()
      elif choose_menu == '2':
         customer_data()
      elif choose_menu == '3':
         car_data()
      elif choose_menu == '4':
         print("LOGGING OUT")
         exit()
      else:
         print("Invalid input. Try again\n")





def transaction():
   while True:
      print("\n========== TRANSACTION MENU ==========")
      print("1. CREATE RENT TRANSACTION")
      print("2. CREATE RETURN TRANSACTION")
      print("0. BACK TO MAIN MENU")

      show_transaction_table()

      choose_trans = input("Your choice: ")
            
      if choose_trans == '1':
         print("\n========== RENT TRANSACTION ==========")
         rent_transaction()
      
      if choose_trans == '2':
         print("\n========== RETURN TRANSACTION ==========")
         return_transaction()
      
      elif choose_trans == '0':
         menu()
      else:
         print("Invalid input. Try again\n")
   





def customer_data():
   print("========== CUSTOMER DATA MENU ==========")
   print("1. ADD NEW CUSTOMER")
   print("2. SEARCH CUSTOMER BY ID")
   print("3. EDIT CUSTOMER DATA")
   print("4. DELETE CUSTOMER DATA")
   print("0. BACK TO MAIN MENU")
   print("\n========== CUSTOMER DATA TABLE ==========\n")
   print("|Index\t| ID Customer \t| Customer Name \t| Address \t| Phone Number \t\t| ID Number \t| Driver's License")
   for i in range(len(customer_table)):
      print(f'|{i} \t| {customer_table[i]['customer_id']} \t| {customer_table[i]['name']} \t| {customer_table[i]['address']} \t| {customer_table[i]['phone']} \t| {customer_table[i]['KTP']}\t| {customer_table[i]['SIM']}')
   choose_cust = input("Your choice: ")
   
   
   if choose_cust == '1':
      print("========== ADD NEW CUSTOMER ==========")
      create_customer(customer_table)
   
   

   elif choose_cust == '2':
      print("========== SEARCH CUSTOMER BY ID ==========")
      search_by_ID = input("Enter customer ID: ")
      search_customer(search_by_ID)
   

   
   elif choose_cust == '3':
      print("========== EDIT CUSTOMER DATA ==========")
      cust_id = input("Enter customer's ID: ")
      new_name = input("Enter new name (ENTER to skip): ")
      new_address = input("Enter new address (ENTER to skip): ")
      new_phone = input("Enter new phone number (ENTER to skip): ")
      new_IDcard = input("Enter new ID card number (ENTER to skip): ")
      new_license = input("Enter new driver's license number (ENTER to skip): ")
      confirm_edit_cust = input("\nEDIT DATA CUSTOMER? Y/N: ")
      if confirm_edit_cust == 'Y' or 'y':
         update_customer(cust_id, new_name or None, new_address or None, new_phone or None, new_IDcard or None, new_license or None)
      elif confirm_edit_cust == 'N' or 'n':
         print("Back to main menu")
      else:
         print("Invalid input. Try again\n")
   

   
   elif choose_cust == '4':
      print("========== DELETE CUSTOMER DATA ==========")
      index_cust = int(input("Enter customer's index: "))
      del_choose= (input(f"Delete {index_cust} customer? Y/N: "))
      if del_choose == 'Y' or 'y':
         del customer_table[index_cust]
         print("Deleted")
      elif del_choose == 'N' or 'n':
         print("Back to main menu")
      else:
         print("Invalid input. Try again\n")
   
   

   elif choose_cust == '0':
      menu()
   else:
      print("Invalid input. Try again\n")






def car_data():
   print("========== CAR DATA MENU ==========")
   print("1. CREATE NEW CAR DATA")
   print("2. SEARCH CAR BY PLATE")
   print("3. EDIT CAR DATA")
   print("4. DELETE CAR DATA")
   print("0. BACK TO MAIN MENU")
   print("\nCAR DATA TABLE\n")
   print('|Index\t| Plate Numbers \t| Brand \t| Type \t\t| Price \t| Status  ')
   for i in range(len(cars_table)):
      print(f'|{i} \t| {cars_table[i]['plate_number']}| {cars_table[i]['brand']} \t| {cars_table[i]['type']} \t| {cars_table[i]['price']} \t| {cars_table[i]['status']}')
   choice_car = input("Your choice: ")
   
   
   if choice_car == '1':
      print("========== CREATE NEW CAR DATA ==========")
      create_car(cars_table)


   elif choice_car == '2':
      print("========== SEARCH CAR BY PLATE==========")
      search_by_plate = input("Enter plate number you want: ")
      search_car(search_by_plate)


   elif choice_car == '3':
      print("========== EDIT CAR ==========")
      plate_numb = input("Enter plate number: ")
      new_brand = input("Enter new brand (ENTER to skip): ")
      new_type = input("Enter new type (ENTER to skip): ")
      new_price = input("Enter new price (ENTER to skip): ")
      new_status = input("AVAILABLE / NOT AVAILABLE (ENTER to skip): ")
      
      confirm_edit_car = input("SUBMIT? Y/N: ")
      if confirm_edit_car == 'Y' or 'y':
         update_car(plate_numb, new_brand or None, new_type or None, new_price or None, new_status or None)
      elif confirm_edit_car == 'N' or 'n':
         print("Back to main menu\n")
      else:
         print("Invalid input. Try again\n")


   elif choice_car == '4':
      print("========== DELETE CAR DATA ==========")
      car_idx = int(input("Enter car's index: "))
      confirm_del_car = (input(f"Delete {car_idx} car? Y/N: "))
      if confirm_del_car == 'Y' or 'y':
         del cars_table[car_idx]
         print("Deleted")
      elif confirm_del_car == 'N' or 'n':
         print("Back to main menu")
      else:
         print("Invalid input. Try again\n")


   elif choice_car == '0':
      menu()
   else:
      print("Invalid input. Try again\n")

if __name__ == "__main__":
   menu()