class Review:
    def __init__(self, id, customer_id, restaurant_id, star_rating, conn=None):
        self.id = id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating = star_rating
        self.conn = conn  # Initialize database connection

    def customer(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id=?', (self.customer_id,))
        customer_data = cursor.fetchone()
        return Customer(customer_data[0], customer_data[1], customer_data[2])

    def restaurant(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM restaurants WHERE id=?', (self.restaurant_id,))
        restaurant_data = cursor.fetchone()
        return Restaurant(restaurant_data[0], restaurant_data[1], restaurant_data[2])

    def full_review(self):
        customer = self.customer()
        restaurant = self.restaurant()
        return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."
