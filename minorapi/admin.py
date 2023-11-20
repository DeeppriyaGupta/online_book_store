from django.contrib import admin
from minorapi.models import Book, User, Issued

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['book_id', 'book_name', 'book_edition', 'book_author']
    search_fields=('book_name',)

class UserAdmin(admin.ModelAdmin):
    list_display=['user_id', 'user_name', 'user_email']
    search_fields=('user_name',)

class IssuedAdmin(admin.ModelAdmin):
    list_display=['book_ref','user_ref', 'get_user_email']
    list_filter=('book_ref', 'user_ref')

    def get_user_email(self, obj):
        return obj.user_ref.user_email

admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Issued, IssuedAdmin)

