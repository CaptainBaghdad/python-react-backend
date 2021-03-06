from rest_framework import serializers
from stocks.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','name', 'email')