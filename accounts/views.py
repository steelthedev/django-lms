from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes


@api_view(["POST",])
def RegisterView(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            data['token']= token
        else:
            data['response'] = "Something went wrong somewhere"
        return Response(data)


@authentication_classes([])
class SFObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        return super(SFObtainAuthToken, self).post(request, *args, **kwargs)
 
