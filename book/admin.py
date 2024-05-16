from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'picture', 'author', 'email', 'describe', 'book_soft_copy']
