from django.contrib import admin
from .models import Book
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns in admin list view
    list_filter = ("publication_year", "author")            # sidebar filters
    search_fields = ("title", "author")                     # search box
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_of_birth", "is_staff")
    
# ✅ Register CustomUser properly
admin.site.register(CustomUser, CustomUserAdmin)