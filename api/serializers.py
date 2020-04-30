from rest_framework import serializers
from customers.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'email', 'company',)
        model = User
