from rest_framework import serializers
from minorapi.models import Book, User, Issued

class BookSerializer(serializers.ModelSerializer):
    # url=serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='book_id')
    class Meta:
        model=Book
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class IssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issued
        fields='__all__'


#user/{does not exist} = giving error
#user/{id}/all_assigned_books
#put and active state in issued
#instead of reference show name in issued