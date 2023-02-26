from rest_framework import serializers
from friends.models import Friend

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        field = '__all__'