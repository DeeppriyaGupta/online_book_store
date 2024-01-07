from django.urls import path, include
from minorapi.views import BookView,  BookById, FavoriteListCreateView, UserFavoriteBooksView, IsFavoriteView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

# router=routers.DefaultRouter()
# router.register(r'book',BookView, basename='book')
# router.register(r'user', UserView, basename='user')
# router.register(r'issued', IssuedView, basename='issued')
# router.register(r'api', CustomObtainAuthToken)

# # urlpatterns=[
# #     path('', include(router.urls))
# # ]



urlpatterns = [
    # path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('books/', BookView.as_view()),
    path('books/<int:pk>', BookById.as_view()),
    path('favorites/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('user/<int:user_id>/favorites/', UserFavoriteBooksView.as_view(), name='user-favorite-books'),
    path('isfavorite/user/<int:user_id>/book/<int:book_id>/', IsFavoriteView.as_view(), name='is-favorite')
    # path('user/', UserView.as_view()),
    # path('user/<int:pk>', UserById.as_view()),
    # path('issued/', IssuedView.as_view()),
    # path('register/', UserRegistration.as_view(), name='user-registration'),
    # path('login/', UserLogin.as_view(), name='user-login'),

    # path('user/<str:data>', UserByName.as_view())
    # path('users/', UserView.as_view({'get': 'list'}), name='user-list'),
    # path('issued/', IssuedView.as_view({'get': 'list'}), name='issued-list'),
]

urlpatterns=format_suffix_patterns(urlpatterns)

# urlpatterns=[
#     path('books/', BookView, name='book-view')
# ]