import sqlite3

class Restaurant:
    def __init__(self, id, name, price, conn=None):
        self.id = id
        self.name = name
        self.price = price
        self.conn = conn

    def reviews(self):
        # Import Review here where needed to avoid circular dependency
        from Review import Review
        
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM reviews WHERE restaurant_id=?', (self.id,))
        reviews = cursor.fetchall()
        return [Review(review[0], review[1], review[2], review[3], self.conn) for review in reviews]

    def customers(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT DISTINCT customer_id FROM reviews WHERE restaurant_id=?', (self.id,))
        customer_ids = [row[0] for row in cursor.fetchall()]
        # Import Customer here where needed to avoid circular dependency
        from Customer import Customer
        return [Customer(customer_id, None, None, self.conn) for customer_id in customer_ids]

    @classmethod
    def fanciest(cls, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM restaurants ORDER BY price DESC LIMIT 1')
        restaurant_data = cursor.fetchone()
        if restaurant_data:
            return Restaurant(restaurant_data[0], restaurant_data[1], restaurant_data[2], conn)
        else:
            return None

    def all_reviews(self):
        reviews = self.reviews()
        return [review.full_review() for review in reviews]
