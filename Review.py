class Review:
    def __init__(self, id, customer_id, restaurant_id, star_rating, conn=None):
        self.id = id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating
        self.conn = conn

    def customer(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id=?', (self.customer_id,))
        customer_data = cursor.fetchone()
        # Import Customer here where needed to avoid circular dependency
        from Customer import Customer
        return Customer(customer_data[0], customer_data[1], customer_data[2], self.conn)

    def restaurant(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM restaurants WHERE id=?', (self.restaurant_id,))
        restaurant_data = cursor.fetchone()
        # Import Restaurant here where needed to avoid circular dependency
        from Restaurant import Restaurant
        return Restaurant(restaurant_data[0], restaurant_data[1], restaurant_data[2], self.conn)

    def full_review(self):
        customer = self.customer()
        restaurant = self.restaurant()
        return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."

    def save(self):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO reviews (customer_id, restaurant_id, star_rating) VALUES (?, ?, ?)',
                       (self.customer_id, self.restaurant_id, self.star_rating))
        self.conn.commit()
