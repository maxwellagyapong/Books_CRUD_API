from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
from rest_framework import status

@api_view(["GET", "POST"])
def book_list(request):

    if request.method == "GET":
        try:
            books = Book.objects.all()
        except Book.DoesNotExist:
            books = None
            if books == None:
                return Response({"Error": "No books found!"}, 
                                status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET","PUT", "DELETE"])
def book_detail(request, pk):

    #Get specific book
    if request.method == "GET":
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            book = None
            if book == None:
                return Response({"Error": "Book not found!"}, 
                                status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # Update Book
    if request.method == "PUT":
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({"Error": "Book not found!"}, 
                            status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete specific book
    if request.method == "DELETE":
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({"Error": "Book not found!"}, 
                            status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        