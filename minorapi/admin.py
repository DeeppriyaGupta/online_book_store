from django.contrib import admin
from minorapi.models import Book, Favorite
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

# admin.site.unregister(User)

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['book_id', 'book_name','book_description', 'book_author', 'book_image', 'rating']
    search_fields=('book_name',)

class FavAdmin(admin.ModelAdmin):
    list_display=['user_id', 'book']
    search_fields=('user_id',)

# class UserAdmin(admin.ModelAdmin):
#     list_display=['username', 'email']
#     search_fields=('username',)

# class IssuedAdmin(admin.ModelAdmin):
#     list_display=['book_ref','user_ref', 'get_user_email']
#     list_filter=('book_ref', 'user_ref')

#     def get_user_email(self, obj):
#         return obj.user_ref.user_email

admin.site.register(Book, BookAdmin)
admin.site.register(Favorite, FavAdmin)
# admin.site.register(User, UserAdmin)
# admin.site.register(Issued, IssuedAdmin)

