from unicodedata import name
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name= "accounts"

urlpatterns = [
    path('signup', views.RegisterView, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('api/v1/', include('djoser.urls.authtoken')),
   
]