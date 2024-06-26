# BISMILLAH
# /==========  CAPSTONE PROJECT    ==========/
# /========== AZALIA ANANDA ARINAL ==========/
# /==========     RENTAL MOBIL     ==========/

from datetime import datetime

# /==================== DATA ====================/

cars_table = [
   {
      'plate_number' : 'L 21 A',
      'brand' : 'FIAT MOBILE',
      'type' :'FIAT 500',
      'price' : 500000,
      'status' : 'AVAILABLE'
   },
   {
      'plate_number' : 'L 21 C',
      'brand' : 'TESLA',
      'type' :'CYBERTRUCK',
      'price' : 1000000,
      'status' : 'AVAILABLE'
   },
   {
      'plate_number' : 'L 98 E',
      'brand' : 'PEUGEOT',
      'type' :'205 GTI',
      'price' : 750000,
      'status' : 'AVAILABLE'
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

transaction_table= []

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
   for transaction in transaction_table:
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
    search_result = [i for i in customer_table if i['customer_id'].lower() == search_by_ID.lower()]
    if not search_result:
        print("Customer not found", search_by_ID)
    else:
      print("| ID Customer \t| Customer Name \t| Address \t| Phone Number \t\t| ID Number \t| Driver's License")
      for i in search_result:
         print(f'| {i['customer_id']} \t| {i['name']} \t| {i['address']} \t| {i['phone']} \t| {i['KTP']}\t| {i['SIM']}')




def search_car(search_by_plate):
    search_result = [i for i in cars_table if i['plate_number'].lower() == search_by_plate.lower()]
    if not search_result:
        print("Car not found", search_by_plate)
    else:
      print('| Plate Numbers | Brand \t| Type \t\t| Price \t| Status  ')
      for i in search_result:
         print(f'| {i['plate_number']}\t| {i['brand']} \t| {i['type']} \t| {i['price']} \t| {i['status']}')






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



# /==================== DELETE ====================/
def delete_customer(car_table):
   try:
      index_cust = int(input("Enter customer's index: "))
      if index_cust < 0 or index_cust >=len(customer_table):
         print("Index is not valid")
         return
   except ValueError:
         print("Index is not valid")
         return
   
   del_choose= (input(f"Delete customer {index_cust}? Y/N: "))
   if del_choose == 'Y' or 'y':
      del customer_table[index_cust]
      print("Deleted")
   elif del_choose == 'N' or 'n':
      print("Back to main menu")
   else:
      print("Invalid input. Try again\n")




def delete_car(cars_table):
   try:
      car_idx = int(input("Enter car index: "))
      if car_idx < 0 or car_idx >=len(cars_table):
         print("Invalid car index")
         return
   except ValueError:
      print("Invalid input")
      return
   
   confirm_del_car = (input(f"Delete car {car_idx} ? Y/N: "))
   if confirm_del_car == 'Y' or 'y':
      del cars_table[car_idx]
      print("Car data deleted")
   elif confirm_del_car == 'N' or 'n':
      print("Back to main menu")
   else:
      print("Invalid input. Try again\n")



# /==================== TRANSACTION ====================/
def rent_transaction():
   rent_id = input("Enter new rent ID: ")

   # input plate number
   while True:
      plate_numb = input("Enter car's plate number: ")
      i = validate_car_id(plate_numb)
      if i and i['status'] == 'AVAILABLE':
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

   print(f"Total Amount: {total_amount}")

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
      transaction_table.append(transaction)
      print("Rent transaction added")
   else:
      print("Cancel transaction")




late_fee = 200000

def calculate_late_fee(late_days, daily_rent):
    daily_penalty = daily_rent * late_fee
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
         late_fee_count = calculate_late_fee(late_days, transaction['total'])

   # total_amount_late = transaction['total'] + late_fee_count
   # print(f'Total Amount: {total_amount_late}')

   confirm_return = input("Submit transaction? Y/N: ")
   if confirm_return == 'Y' or 'y':
      transaction['late_fee'] = late_fee_count

      car = validate_car_id(transaction['plate_number'])
      car['status'] = 'AVAILABLE'

      transaction_table[:] = [t for t in transaction_table if t['rent_id'] != rent_id]

      print ("Return transaction added")
   else:
      print("Cancel transaction")
   
   
   
   
# /==================== SHOW TABLES ====================/
def show_transaction_table():
   if len(transaction_table) == 0:
      print("\nThere is no transaction data\n")
   else:
      print("========== TRANSACTION TABLE ==========\n")
      print('|Rent ID\t| Plate Number \t| Customer ID \t| Start Date \t| End Date \t| Days  | Total Amount')
      for i in range(len(transaction_table)):
         print(f'| {transaction_table[i]['rent_id']} \t| {transaction_table[i]['plate_number']} \t| {transaction_table[i]['customer_id']} \t| {transaction_table[i]['start_rent_count']}\t| {transaction_table[i]['end_rent_count']}\t| {transaction_table[i]['rent_days_count']}\t| {transaction_table[i]['total']}')





# /==================== MENU ====================/
def menu():
   while True:
      print("\n========== MAIN MENU ==========")
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
      
      elif choose_trans == '2':
         print("\n========== RETURN TRANSACTION ==========")
         return_transaction()
      
      elif choose_trans == '0':
         menu()
         break
      else:
         print("Invalid input. Try again\n")
   





def customer_data():
   print("\n========== CUSTOMER DATA MENU ==========")
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
      print("\n========== ADD NEW CUSTOMER ==========")
      create_customer(customer_table)
   
   

   elif choose_cust == '2':
      print("\n========== SEARCH CUSTOMER BY ID ==========")
      search_by_ID = input("Enter customer ID: ")
      search_customer(search_by_ID)
   

   
   elif choose_cust == '3':
      print("\n========== EDIT CUSTOMER DATA ==========")
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
      print("\n========== DELETE CUSTOMER DATA ==========")
      delete_customer(customer_table)


   elif choose_cust == '0':
      menu()
   else:
      print("Invalid input. Try again\n")






def car_data():
   print("\n========== CAR DATA MENU ==========")
   print("1. CREATE NEW CAR DATA")
   print("2. SEARCH CAR BY PLATE")
   print("3. EDIT CAR DATA")
   print("4. DELETE CAR DATA")
   print("0. BACK TO MAIN MENU")
   print("\n========== CAR DATA TABLE ==========\n")
   print('|Index\t| Plate Numbers\t| Brand \t| Type \t\t| Price \t| Status  ')
   for i in range(len(cars_table)):
      print(f'|{i} \t| {cars_table[i]['plate_number']}\t| {cars_table[i]['brand']} \t| {cars_table[i]['type']} \t| {cars_table[i]['price']} \t| {cars_table[i]['status']}')
   choice_car = input("Your choice: ")
   
   
   if choice_car == '1':
      print("\n========== CREATE NEW CAR DATA ==========")
      create_car(cars_table)


   elif choice_car == '2':
      print("\n========== SEARCH CAR BY PLATE==========")
      search_by_plate = input("Enter plate number you want: ")
      search_car(search_by_plate)


   elif choice_car == '3':
      print("\n========== EDIT CAR ==========")
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
      print("\n========== DELETE CAR DATA ==========")
      delete_car(cars_table)


   elif choice_car == '0':
      menu()
   else:
      print("Invalid input. Try again\n")

if __name__ == "__main__":
   menu()