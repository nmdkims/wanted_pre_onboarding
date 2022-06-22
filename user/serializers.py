# from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ['username','password']
