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
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.year = validated_data.get("year", instance.year)
        instance.save()
        return instance