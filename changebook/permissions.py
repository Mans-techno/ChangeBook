from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'Иди от суда'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsTradeParticipant(BasePermission):
    message = 'Иди от суда'
    def has_object_permission(self, request, view, obj):
        return request.user == obj.sender or request.user == obj.book.owner


class IsAuthorOrReadOnly(BasePermission):
    message = 'Иди от суда'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
