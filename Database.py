class Database:
    def __init__(self, conn):
        self.conn = conn

    def create_restaurants_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def create_customers_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_reviews_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                restaurant_id INTEGER,
                star_rating INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
            )
        ''')
        self.conn.commit()

