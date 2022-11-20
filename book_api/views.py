# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# # relative imports
# from book_api.models import Book
# from book_api.serializer import Book_Serializer

# # Create your views here.

# #/books/list/
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all() #Complex data
#     serializer = Book_Serializer(books, many=True)
#     return Response(serializer.data)

# #/books
# @api_view(['POST'])
# def book_create(request):
#     serializer = Book_Serializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #/books/<int:pk>
# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:    
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Book does not exist'
#         }, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = Book_Serializer(book)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = Book_Serializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# relative imports
from book_api.models import Book
from book_api.serializer import BookSerializer

#/books/list/
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all() #Complex data
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
#/books
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#/books/<int:pk>
class BookDetail(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Book does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
            'error': 'Book does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({
            'error': 'Book does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)