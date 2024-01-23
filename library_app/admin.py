from django.contrib import admin
from .models import Book, registration_table
# Register your models here.

admin.site.register(Book)
admin.site.register(registration_table)
