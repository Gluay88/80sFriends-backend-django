from friends.models import Friend
from django.http import JsonResponse
from friends.serializers import FriendSerializer

def friends(request):
    #invoke serializer and return to client
    data = Friend.objects.all()
    serializer = FriendSerializer(data, many=True)
    return JsonResponse({'friends': serializer.data})