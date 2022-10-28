from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from login.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

#generate token manaually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#creating a class for registering the user using serializer
class UserRegistration(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
            #getting token and storing it into a var
            token = get_tokens_for_user(user)  
            return Response({'token':token,'msg':'Registration Sucessful'},status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTPS_400_BAD_REQUEST) 


class UserLogin(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Sucessfull'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)


