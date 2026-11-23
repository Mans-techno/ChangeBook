from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .serializers import *
from .permissions import IsOwnerOrReadOnly, IsTradeParticipant, IsAuthorOrReadOnly
from .filters import BookFilter, TradeFilter
# Create your views here.


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CityListCreateView(ListCreateAPIView):
    queryset = City.objects.order_by('id')
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.order_by('id')
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.filter(is_available=True).select_related('owner', 'category', 'city').order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['name', 'author']
    ordering_fields = ['created_at', 'name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TradeListCreateView(ListCreateAPIView):
    serializer_class = TradeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TradeFilter

    def get_queryset(self):
        user = self.request.user
        return Trade.objects.filter(Q(sender=user) | Q(book__owner=user)).select_related('sender', 'book', 'offered_book').order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class TradeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [IsAuthenticated, IsTradeParticipant]


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.select_related('author', 'user').order_by('-id')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

