class Customer:
    def __init__(self, id, first_name, last_name, conn=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.conn = conn

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        from Restaurant import Restaurant  
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT r.* FROM reviews
            JOIN restaurants r ON reviews.restaurant_id = r.id
            WHERE customer_id = ?
            GROUP BY r.id
            ORDER BY AVG(star_rating) DESC
            LIMIT 1
        ''', (self.id,))
        restaurant_data = cursor.fetchone()
        if restaurant_data:
            return Restaurant(restaurant_data[0], restaurant_data[1], restaurant_data[2])

    def add_review(self, restaurant, rating):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO reviews (customer_id, restaurant_id, star_rating) VALUES (?, ?, ?)',
                       (self.id, restaurant.id, rating))
        self.conn.commit()

    def delete_reviews(self, restaurant):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM reviews WHERE customer_id=? AND restaurant_id=?', (self.id, restaurant.id))
        self.conn.commit()
