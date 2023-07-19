from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

@api_view(["GET", "POST"])
def book_list(request):

    if request.method == "GET":
        try:
            books = Book.objects.all()
        except Book.DoesNotExist:
            raise("Books not found!")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)