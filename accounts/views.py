
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from .serializers import ProfileSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Profile
from rest_framework import status, authentication, permissions
from order.serializers import *
from order.models import *

@api_view(["POST",])
def RegisterView(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.refresh_from_db()
            account.profile.username = account.username
            account.profile.first_name = account.first_name
            account.profile.last_name = account.last_name
            account.email = account.email
            account.save()
        else:
            return HttpResponse( status = 201 )
        return HttpResponse( status = 200 )


@authentication_classes([])
class SFObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        return super(SFObtainAuthToken, self).post(request, *args, **kwargs)


@api_view(["GET","PUT"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def ProfileView(request):
    if request.method == "GET":
        try:
            profile = Profile.objects.get(user = request.user)
        except:
            return HttpResponse( status = 201 )
        serializer = ProfileSerializer(profile, many = False)
        return Response(serializer.data)


@api_view(["PUT","PATCH"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def ProfileEdit(request):
    if request.method == "PATCH":
        try:
            profile = Profile.objects.get(user = request.user)
        except:
            return HttpResponse( status = 201 )
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status = 200)
        return Response(serializer.data)

@api_view(["PUT","PATCH"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def ProfilePictureEdit(request):
    if request.method == "PATCH":
        try:
            profile = Profile.objects.get(user = request.user)
        except:
            return HttpResponse( status = 201 )
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status = 200)
        return Response(serializer.data)



@api_view(["GET"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def MyCourseView(request):
    if request.method == "GET":
        try:
            order = Order.objects.filter(user = request.user)
        except:
            return HttpResponse( status = 400 )
        serializer = MyOrderSerializer(order, many = True)
        return Response(serializer.data)
  