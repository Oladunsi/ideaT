from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .models import User

# Create your views here.


class RegistrationView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request,*args, **kwargs):
        serializerClass = RegisterSerializer(request.data)
        if serializerClass.is_valid():
            firstName = serializerClass.data.get('firstName')
            lastName = serializerClass.data.get('lastName')
            phoneNumber = serializerClass.data.get('phoneNumber')
            email = serializerClass.data.get('email')
            avatar = serializerClass.data.get('avatar')
            passtoken = serializerClass.data.get('passtoken')
            queryset = queryset = User.objects.filter(Email=serializerClass.request.get('Email'))
            if queryset.exists():
                return Response({'Bad Request': 'Email entered exists'},status=status.HTTP_400_BAD_REQUEST)
             
            newUser = User(firstName=firstName,lastName=lastName,phoneNumber=phoneNumber,email=email,avatar=avatar,passtoken=passtoken)
            newUser.save()
            return Response(RegisterSerializer(newUser).data,status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid entry....'},status=status.HTTP_400_BAD_REQUEST)