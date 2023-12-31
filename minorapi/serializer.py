from rest_framework import serializers
from minorapi.models import Book, Favorite
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'





# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     # confirm_password=serializers.CharField(style={'input_type':'password'}, write_only=True)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
        

# class BookSerializer(serializers.ModelSerializer):
#     # url=serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='book_id')
#     class Meta:
#         model=minorapi_book
#         fields='__all__'

#     # def to_representation(self, instance):
#     #     representation = super().to_representation(instance)
#     #     representation['book_ref'] = instance.book_ref.book_name
#     #     representation['user_ref'] = instance.user_ref.user_name
#     #     return representation

# class IssuedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Issued
#         fields='__all__'