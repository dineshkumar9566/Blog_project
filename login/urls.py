from django.urls import path
from . views import UserRegistration, LoginView, RefreshTokenView, UserDetails

urlpatterns = [
     path('v1/register/', UserRegistration.as_view()),    # URL for user registration
     path('v1/login/', LoginView.as_view()),         # URL for user login
     path('v1/refresh/', RefreshTokenView.as_view()),    # URL for refreshing access tokens
     path('v1/user/', UserDetails.as_view()),     #URL for user details     
    #  path('v1/logout/', LogoutView.as_view()),     #URL for logout 
]    