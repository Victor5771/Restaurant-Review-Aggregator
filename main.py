import sqlite3
from Customer import Customer
from Restaurant import Restaurant

def main():
    # Create a database connection
    conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your actual database file

    # Example instantiation of classes
    customer1 = Customer(1, 'John', 'Doe', conn)
    restaurant1 = Restaurant(1, 'Restaurant A', 10, conn)

    # Test methods requiring database connection
    print(customer1.full_name())
    print(restaurant1.fanciest())

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
