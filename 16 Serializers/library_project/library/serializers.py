from rest_framework import serializers
from .models import Author, Book


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'isbn']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'books']


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True
    )
    author_details = AuthorSerializer(source='author', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_id', 'author_details', 'published_date', 'isbn']

    def create(self, validated_data):
        author = validated_data.pop('author_id')
        return Book.objects.create(author=author, **validated_data)

    def update(self, instance, validated_data):
        author = validated_data.pop('author_id', None)
        if author:
            instance.author = author

        instance.title = validated_data.get('title', instance.title)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance
