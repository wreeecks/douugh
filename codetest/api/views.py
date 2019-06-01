from django.utils.crypto import get_random_string

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ApiUser
from .serializers import ApiUserSerializer, ApiUserLoginSerializer


# Create your views here.
class ApiUserView(generics.ListCreateAPIView):
    """
    API endpoint to view or create user
    """
    queryset = ApiUser.objects.all()
    serializer_class = ApiUserSerializer

    
class ApiUserLoginView(APIView):
    """
    API endpoint for user login
    """
    serializer_class = ApiUserLoginSerializer

    def post(self, request, *args, **kwargs):
        """
        validate and generate token
        """
        user = ApiUser.objects.filter(email=request.data['email'], password=request.data['password'])
        
        if user:
            token = get_random_string(length=32) 
            return Response({'token': token})
        else:
            return Response('invalid user', status=401)
        
