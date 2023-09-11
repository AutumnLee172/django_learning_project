from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myuser = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse(template.render(context, request))

class UserApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # users = User.objects.all().filter(user = request.user.id)
        # serializer = UserSerializer(users, many=True)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'email': request.data.get('email'), 
            'username': request.data.get('username'), 
            'password': request.data.get('password')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginApi(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    # 2. Login
    def post(self, request, *args, **kwargs):
        
        email = request.data.get('email')
        password = request.data.get('password')

        isCorrect = User.objects.filter(email = email, password = password).exists()
        if isCorrect:
            return Response(1, status=status.HTTP_200_OK)
        else:
            return Response(0, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
