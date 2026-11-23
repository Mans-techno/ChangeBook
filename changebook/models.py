from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_condition = [
        ('New', 'Новый'),
        ('Good', 'Хорошая'),
        ('Middle', 'Средная'),
        ('Bad', 'Плохая'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    condition = models.CharField(max_length=20, choices=book_condition)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Trade(models.Model):
    trade_status = [
        ('pending', 'Ожидает'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонён'),
        ('cancelled', 'Отменён'),
    ]
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trades')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='trades')  # чужая книга
    offered_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='offers')  # моя книга
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=trade_status, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Review(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_reviews')  # кто пишет
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  # о ком отзыв
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.rating
