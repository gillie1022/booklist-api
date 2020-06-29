from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from api.models import User, Book, Author, Note
from api.serializers import UserSerializer, BookSerializer, AuthorSerializer, NoteSerializer
from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['status']

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = BookFilter
    
    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]