import sqlite3
from Customer import Customer
from Restaurant import Restaurant
from Review import Review
from Database import Database

def add_customer(conn):
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    customer = Customer(None, first_name, last_name, conn)
    customer.save()

def add_review(conn):
    customer_id = int(input("Enter customer ID: "))
    restaurant_id = int(input("Enter restaurant ID: "))
    star_rating = int(input("Enter star rating: "))
    review = Review(None, customer_id, restaurant_id, star_rating, conn)
    review.save()

def main():
    conn = sqlite3.connect('your_database.db')
    db = Database(conn)
    db.create_restaurants_table()
    db.create_customers_table()
    db.create_reviews_table()

    while True:
        print("\n1. Add Customer")
        print("2. Add Review")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer(conn)
        elif choice == '2':
            add_review(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
