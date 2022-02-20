from pyexpat import model
from rest_framework import serializers

from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def save(self):
        account = User(
            username = self.validated_data['username'],
            first_name = self.validated_data['username'],
            last_name = self.validated_data['username']

        )

        password = self.validated_data['password']
        
        if not password:
            raise serializers.ValidationError({'password':"passwords must match"})

        account.set_password(password)
        account.save()
        return account