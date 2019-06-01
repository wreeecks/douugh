from rest_framework import serializers
from .models import ApiUser


class ApiUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = ApiUser
        fields = ('id','email','password','first_name','last_name',)


class ApiUserLoginSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    
    class Meta:
        model = ApiUser
        fields = ('email','password')


