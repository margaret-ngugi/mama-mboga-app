#Reviews

class Review:
    reviews = []
    def __init__(self, review_id, user_id, product_id, comment, review_date):
        self.review_id = review_id
        self.user_id = user_id
        self.product_id = product_id
        self.comment = comment
        self.review_date = review_date
    def add_review(self):
        if self.review_id in self.reviews:
            return "Review ID already exists."
        
        else:
            self.reviews.append(self)
            return "Review added successfully."
    def update_review(self):
        if self.review_id not in self.reviews:
            return "Review ID does not exist."
        
        self.reviews[self.review_id] = self
        return "Review updated successfully."
    def delete_review(self):
        if self.review_id not in self.reviews:
            return "Review ID does not exist."
        else:
            self.reviews.remove(self)
            return "Review deleted successfully."
            
review = Review(review_id=7, user_id=4, product_id=6, comment="Waoh this is a wondarful product!", review_date="2023-06-11")
updated_review=review.update_review()
print(updated_review)

deleted_review=review.delete_review()
print(deleted_review)

added_review=review.add_review()
print(added_review)