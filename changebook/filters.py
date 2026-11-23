import django_filters
from .models import Book, Trade


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'category', 'condition', 'city']


class TradeFilter(django_filters.FilterSet):
    class Meta:
        model = Trade
        fields = ['status']
