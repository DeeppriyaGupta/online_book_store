from django.db import models

class Book(models.Model):
    book_id= models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50)
    book_edition=models.IntegerField()

    def __str__(self):
        return self.book_name
    
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField(max_length=50, default='abc@gmail.com')

    def __str__(self):
        return self.user_name

class Issued(models.Model):
    book_ref= models.ForeignKey(Book, on_delete=models.CASCADE)
    user_ref=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Book: {self.book_ref.book_name}, User: {self.user_ref.user_name}'