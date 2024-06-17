from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer
from .models import Token
from rest_framework_simplejwt.tokens import RefreshToken, TokenError # Import TokenError
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .models import Token  # Import the Token model
from jwt.exceptions import ExpiredSignatureError  # Import ExpiredSignatureError
from rest_framework import serializers

# Registration View
class UserRegistration(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        response_data = {}  # Initialize an empty response dictionary
        try:
            if serializer.is_valid():
                serializer.save()
                response_data["status"] = "1"  # Registration succeeded
                response_data["message"] = "Registered successfully"
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data["status"] = "0"  # Registration failed
                response_data["message"] = "Registration failed"
                response_data["message"] = serializer.errors
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login View 
class LoginView(APIView):
    permission_classes = [AllowAny]


    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        response_data = {}  # Initialize an empty response dictionary

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)

                # Create and save tokens in the database
                token, created = Token.objects.get_or_create(user=user)
                token.refresh_token = str(refresh)

                token.access_token = str(refresh.access_token)
                token.save()

                response_data["status"] = "1"  # Login succeeded
                response_data["message"] = 'Logged in successfully'
                response_data["username"] =  user.username
                response_data["refresh"] = str(refresh)

                response_data["access"] = str(refresh.access_token)
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data["status"] = "0"  # Login failed
                response_data["message"] = "Invalid credentials"
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response_data["status"] = "0"  # Login failed
            response_data["message"] = "Both email and password are required"
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


# Refresh token View
class RefreshTokenView(APIView):
    permission_classes = (AllowAny,)  # Remove IsAuthenticated

    def post(self, request):
        refresh_token = request.data.get('refresh')
        response_data = {}  # Initialize an empty response dictionary

        if not refresh_token:
            response_data['status'] = '0'  # Refresh token missing
            response_data['message'] = 'Refresh token is required'
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = Token.objects.get(refresh_token=refresh_token)
            new_access_token = None

            try:
                refresh = RefreshToken(refresh_token)
                new_access_token = str(refresh.access_token)

                # Update the existing token record with the new access token
                token.access_token = new_access_token
                token.save()

            except ExpiredSignatureError:  # Handle ExpiredSignatureError
                pass

            if new_access_token:
                response_data['status'] = '1'  # Refresh succeeded
                response_data['access'] = new_access_token
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data['status'] = '0'  # Refresh failed
                response_data['message'] = 'Invalid refresh token'
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

        except Token.DoesNotExist:
            response_data['status'] = '0'  # Refresh failed
            response_data['message'] = 'Invalid refresh token'
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
        except TokenError as e:  # Handle TokenError
            response_data['status'] = '0'  # Refresh failed
            response_data['message'] = str(e)
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
                
# Get User details
class UserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
            user = request.user
            data = {
                'username': user.username,
                'email': user.email,
                'contact_number': user.contact_number,
                # Add other user details as needed
            }
            return Response(data)

# # Logout
# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         response_data = {}  # Initialize an empty response dictionary

#         try:
#             refresh_token = request.data['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             response_data["status"] = "1"  # Logout succeeded
#             response_data["message"] = 'Successfully logged out'
#             return Response(response_data, status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             response_data["status"] = "0"  # Logout failed
#             response_data["message"] = 'Invalid refresh token'
#             return Response(response_data, status=status.HTTP_400_BAD_REQUEST)