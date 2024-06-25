# Python CRUD Application for Car Rental.

This project is a command-line application made in Python for managing a car rental system. It provides essential CRUD (Create, Read, Update, Delete) functionalities for cars, customers, and transaction.

## Business Understanding

This Python-based car rental system is designed for small to medium-sized businesses in the automotive rental industry, offering tools for owners and managers to streamline operations, optimize inventory and transaction. It enables rental agents to efficiently handle rent transaction, while providing administrative system with simplified processes for record-keeping, and payment processing.

**Benefits:**

* Efficiency and Organization:

Centralizes vehicle, customer, and rental transaction data in a structured database.
Reduces manual paperwork and minimizes errors, enhancing operational efficiency.

* Improved Customer Service:

Enables quick access to customer and vehicle information for rental agents.
Facilitates faster service, personalized interactions, and increased customer satisfaction.

* Financial Management:

Tracks rental transactions and vehicle availability for better financial planning.


**Target Users:**

This Python-based car rental management system streamlines operations for small to medium-sized businesses, facilitating efficient oversight, inventory management, and administrative tasks like record-keeping, and payments.

## Features

* **Create:**
    * Add new rent transaction, return transaction, cars and customers to the system.
* **Read:**
    * View details of cars, customers, and transaction.
* **Update:**
    * Modify information of existing cars and customers.
* **Delete:**
    * Remove cars and customers from the system.

## Installation

1. **Prerequisites:**
    * Python version 3.12.3

2. **Installation:**
    ```bash
    git clone [https://github.com/]https://github.com/AzaliaArinal/Car-Rental-Python-CRUD.git
    cd Car-Rental-Python-CRUD
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Functionality**
    * **Managing Cars:** Add new cars with details such as car's plate number, make, type, availability and rental price. Update existing car information like availability or rental price. Delete cars that are no longer in the fleet.
    * **Managing Customers:** Add new customers with details including customers ID, name, contact information, and address. Update customer information such as contact details. Delete customers who no longer have active rentals.
    * **Managing Transaction:** Add new transaction with details including transaction ID, car's plate number, customer ID, start rent date, end rent date, late returning date.


## Data Model
cars Table:

Fields: plate_number (Primary Key), make(STR), type(STR), rental_price(INT), availability(STR)
Stores information about each car available for rent.


customers Table:

Fields: customer_id (Primary Key), name (STR), address(STR), phone(INT), contact information(INT) 
Stores details of each customer who rents cars.


rentals Table:

Fields: rent_id (Primary Key), plate_number(STR), customer_id(STR), rental_start_date(DATE), rental_end_date(DATE), total_cost(INT), late_fee(INT)
Tracks rental transactions, including which customer rented which car for specific periods and associated costs.


## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [azaliarinal@gmail.com] or submit an issue if you encounter any problems or have suggestions for improvements.

