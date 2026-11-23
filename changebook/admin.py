from django.contrib import admin
from .models import Category, City, Book, Trade, Review

# Register your models here.
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Book)
admin.site.register(Trade)
admin.site.register(Review)
