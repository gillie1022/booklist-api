from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from api.models import User, Book, Author, Note
from api.serializers import UserSerializer, BookSerializer, AuthorSerializer, NoteSerializer

# class isOwner(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.method in permissions.SAFE_METHODS or (request.user and request.user.is_authenticated))

#     def has_object_permission(self, request, view, obj):
#         return bool(request.user and request.user.is_authenticated
#                     and obj.user == request.user)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]