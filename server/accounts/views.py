from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# from .models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.core import serializers

from movies.models import Actor
from .serializers import UserSerializer, ActorSerializer, ActorSerializer2

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def follow(request, username):
    you = get_object_or_404(get_user_model(), username=username)
    me = get_object_or_404(get_user_model(), username=request.data.get('me'))
    ez_real = request.data.get('ez_real')
    followed = True
    if you != me:
        if you.followers.filter(pk=me.pk).exists():
            followed = True
            if ez_real:
                you.followers.remove(me)
                followed = False
        else:
            followed = False
            if ez_real:
                you.followers.add(me)
                followed = True
    wanna_see = serializers.serialize('json', you.followers.all()) 
    # print(wanna_see)
    context = {
        'followed': followed,
        'followers': wanna_see,
        'followers_count': you.followers.count(),
        'followings_count': you.followings.count(),
    }
    return JsonResponse(context, safe=False)

@api_view(['GET', 'POST'])
def set_my_id(request):
    user = get_object_or_404(get_user_model(), username=request.data.get('me'))
    return JsonResponse({ 'user_id': user.id })

@api_view(['GET', 'POST'])
def get_my_actors(request, user_pk):
    # me = get_user_model().objects.filter(like_actors=user_pk)
    my_actors = Actor.objects.filter(like_users=user_pk)

    my_actor_list = []
    for i in range(len(my_actors)):
        serializer = ActorSerializer(my_actors[i])
        my_actor_list.append(serializer.data)
    # print(serializer.data)
    # print(my_actor_list)
    return JsonResponse({'my_actor_list': my_actor_list})

@api_view(['GET','POST'])
def like_this_actor(request, user_pk, actor_pk):
    is_put = request.data.get('is_put')
    user = get_object_or_404(get_user_model(), pk=user_pk)
    actor = get_object_or_404(Actor, actor_id=actor_pk)
    # print(user,actor)
    if is_put:
        if user.like_actors.filter(actor_id=actor_pk).exists():
            # print('이미있음!')
            pass
        else:
            # 없어서 추가하는 부분
            user.like_actors.add(actor)
    else:
        if user.like_actors.filter(actor_id=actor_pk).exists():
            # print('있는데 뺄 예정임!')
            user.like_actors.remove(actor)
        else:
            pass
            # print('없는데도 뺄 생각임!')
    return JsonResponse({1:1})

@api_view(['GET'])
def get_actors_for_check(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer2(actors, many=True)
    return Response(serializer.data)
