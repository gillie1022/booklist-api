from rest_framework import serializers
from api.models import User, Author, Book, Note

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['author']

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['book', 'note', 'page_number', 'created_on']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, required=False)
    
    def create(self, validated_data):
        authors = validated_data.pop('authors', [])
        book = Book.objects.create(**validated_data)
        for author in authors:
            book.authors.create(**author)
        return book

    def update(self, instance, validate_data):
        book = instance
        authors = validate_data.pop('authors', [])
        for key, value in validate_data.items():
            setattr(book, key, value)
        book.save()

        book.authors.all().delete()
        for author in authors:
            book.authors.create(**author)
        return book

    class Meta:
        model = Book
        fields = ['url', 'title', 'authors', 'status', 'notes']