from django.shortcuts import render
from minorapi.serializer import BookSerializer, FavoriteSerializer
from minorapi.models import Book, Favorite
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics


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


class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        if user_id:
            favorites = Favorite.objects.filter(user_id=user_id)
            book_names = [favorite.book.name for favorite in favorites]
            return Response({'user_id': user_id, 'favorite_books': book_names}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'user_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        book_id= request.data.get('book')

        print(f"Received data: {request.data}")
        print(f"Received user_id: {user_id}, book_id: {book_id}")

        if user_id and book_id:
            try:
                book_instance = Book.objects.get(pk=book_id)
                favorite, created = Favorite.objects.get_or_create(user_id=user_id, book=book_instance)
                if not created:
                    favorite.delete()
                    return Response({'message': 'Book unfavorited successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Book favorited successfully'}, status=status.HTTP_201_CREATED)
            except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'user_id and book are required'}, status=status.HTTP_400_BAD_REQUEST)


class UserFavoriteBooksView(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Favorite.objects.filter(user_id=user_id)


# class UserRegistration(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]

#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if email is None or password is None:
#             return Response({'error': 'Both email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Incorrect email or password.'}, status=status.HTTP_401_UNAUTHORIZED)



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



# class UserView(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # basename='user'

# class UserView(APIView):
#     def get(self, request):
#         queryset=User.objects.all()
#         serializer=UserSerializer(queryset, many=True)
#         return Response(serializer.data)
    
    # def post(self, request):
    #     serializer=UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    
# class UserById(APIView):
#     def get(self, request, pk):
#         try:
#             queryset=User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             Response({'error':'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
#             serializer=UserSerializer(queryset)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         queryset=User.objects.get(pk=pk)
#         serializer=UserSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
#     def delete (self, request, pk):
#         queryset=User.objects.get(pk=pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])    
# def createUser(request):
#     if request.method =='POST':
#         serializer=UserSerializer(data=request.data)
#         serializer.save()
#         return serializer.data
# class CreateUser(APIView):
#     def post(self, request):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             email=serializer.validated_data['user_email']
#             if User.objects.filter(user_email=email).exists():
#                 return Response({'detail': 'User already exists.'}, status=status.HTTP_208)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200)
#         return Response(serializer.errors)

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

# class IssuedView(APIView):
#     def get(self, request):
#         queryset=Issued.objects.all()
#         serializer=IssuedSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer=IssuedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

