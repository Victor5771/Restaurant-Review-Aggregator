import sqlite3
from Customer import Customer
from Restaurant import Restaurant

def main():
    
    conn = sqlite3.connect('your_database.db')

    
    customer1 = Customer(1, 'John', 'Doe', conn)
    restaurant1 = Restaurant(1, 'Restaurant A', 10, conn)

    
    print(customer1.full_name())
    print(restaurant1.fanciest())

   
    conn.close()

if __name__ == "__main__":
    main()
