from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import User

class Book(models.Model):
    book_id= models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=50)
    book_description=models.CharField(max_length=200)
    book_author=models.CharField(max_length=50)
    book_image=models.CharField(max_length=100, default='abc.png')
    rating=models.FloatField(
        validators=[
         MaxValueValidator(5), MinValueValidator(1),
    ])


    def __str__(self):
        return self.book_name
    
class Favorite(models.Model):
    user_id = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    




# # class User(models.Model):
# #     user_id=models.AutoField(primary_key=True)
# #     user_name=models.CharField(max_length=50)
# #     user_email=models.EmailField(max_length=50, unique=True)

# #     def __str__(self):
# #         return self.user_name

# class Issued(models.Model):
#     book_ref= models.ForeignKey(minorapi_book, on_delete=models.CASCADE)
#     user_ref=models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'Book: {self.book_ref.book_name}, User: {self.user_ref.user_name}'