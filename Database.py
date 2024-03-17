class Database:
    def __init__(self, conn):
        self.conn = conn

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