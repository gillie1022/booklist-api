from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from api.models import User, Book, Author, Note
from api.serializers import UserSerializer, BookSerializer, AuthorSerializer, NoteSerializer
from django_filters import rest_framework as filters

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS
                    and (request.user and request.user.is_authenticated))

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated
                    and obj.user == request.user)

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['status']

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsOwner]
    filterset_class = BookFilter
    
    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]
    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.book.user)
        return queryset

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsOwner]