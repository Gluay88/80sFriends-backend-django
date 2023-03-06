from friends.models import Friend
from django.http import JsonResponse, Http404
from friends.serializers import FriendSerializer

def friends(request):
    #invoke serializer and return to client
    data = Friend.objects.all()
    serializer = FriendSerializer(data, many=True)
    return JsonResponse({'friends': serializer.data})

def friend(request, id):
    try:
        data = Friend.objects.get(pk=id)
    except Friend.DoesNotExist:
        raise Http404("We have fallen apart! 😢 ")
    serializer = FriendSerializer(data)
    return JsonResponse({'friend': serializer.data})