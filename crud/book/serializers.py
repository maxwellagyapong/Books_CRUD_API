from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    author = serializers.CharField()
    year = serializers.DateField()

    class Meta:
        model = Book
        fields = ("id", "title", "author", "year")

    def create(self, validated_data):
        return Book.objects.create(**validated_data)