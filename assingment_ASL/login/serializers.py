from rest_framework import serializers
from login.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    #password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email','name','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
#this will validate the data    
def create(self, validate_data):
    return User.objects.create_user(**validate_data )


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
#required fields for login
        fields = ['email','password'] 
