from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title
    
class UserReviews(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.name}"
    
class Bookpurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    before_purchase_balance = models.DecimalField(max_digits=10, decimal_places=2)
    after_purchase_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase by {self.user.username} - Book: {self.book.title} - Date: {self.purchase_date}"