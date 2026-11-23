from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cities/', CityListCreateView.as_view(), name='city_list_create'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('trades/', TradeListCreateView.as_view(), name='trade_list_create'),
    path('trades/<int:pk>/', TradeDetailView.as_view(), name='trade_detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
]
