from django.shortcuts import render
from minorapi.serializer import BookSerializer, UserSerializer, IssuedSerializer
from minorapi.models import Book, User, Issued
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView

# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         if 'token' in response.data:
#             user = Token.objects.get(key=response.data['token']).user
#             user_id = user.id
#             response.data['user_id'] = user_id
#         return response

# class BookView(viewsets.ModelViewSet):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # basename='book'
#     def get(self, request):
#         return Response(BookView.serializer_class.data)

class BookView(APIView):

    def get(self, request):
        queryset=Book.objects.all()
        serializer=BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
#user/{does not exist} = giving error
class BookById(APIView):

    # def get_book(self, request, pk):
    #     try:
    #         return Book.objects.get(pk=pk)
    #     except Book.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        try:
            get_book_by_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            Response({'error':'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer=BookSerializer(get_book_by_id)
        return Response(serializer.data)

    def put(self, request, pk):
        get_book_by_id=Book.objects.get(pk=pk)
        serializer=BookSerializer(get_book_by_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        get_book_by_id=Book.objects.get(pk=pk)
        get_book_by_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # basename='user'

class UserView(APIView):
    def get(self, request):
        queryset=User.objects.all()
        serializer=UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class UserById(APIView):
    def get(self, request, pk):
        try:
            queryset=User.objects.get(pk=pk)
        except User.DoesNotExist:
            Response({'error':'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset=User.objects.get(pk=pk)
        serializer=UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    def delete (self, request, pk):
        queryset=User.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def get(self, request, pk):
    #     try:
    #         queryset=User.objects.get(pk=pk)
    #         user_all_book=Book.objects.filter(book_ref=queryset)
    #         book_serializer=BookSerializer(user_all_book, many=True, context={'request':request})
    #         return Response(book_serializer.data)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
        
# class UserByName(APIView):
#     def get(self, request, data):
#         try:
#             queryset=User.objects.get(data=request.data)
#         except User.DoesNotExist:
#             Response({'error':'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         serializer=UserSerializer(queryset)
#         return Response(serializer.data)



# class IssuedView(viewsets.ModelViewSet):
#     queryset=Issued.objects.all()
#     serializer_class=IssuedSerializer
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # basename='issued'

class IssuedView(APIView):
    def get(self, request):
        queryset=Issued.objects.all()
        serializer=IssuedSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=IssuedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

