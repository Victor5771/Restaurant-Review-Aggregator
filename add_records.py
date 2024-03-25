import sqlite3
from Database import Database

def add_customer(conn, first_name, last_name):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
    conn.commit()

def main():
    conn = sqlite3.connect('your_database.db')
    db = Database(conn)

    # Create customers table
    db.create_customers_table()

    # Add records
    add_customer(conn, 'John', 'Doe')

    conn.close()

if __name__ == "__main__":
    main()
