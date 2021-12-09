from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from movies.models import Actor

from .serializers import CommentSerializer, ReviewSerializer, ReviewSerializer2
from .models import Review, Comment


# Create your views here.
@api_view(['GET'])
def review_index(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_review(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    # print(reviews.values())
    serializer = ReviewSerializer2(review)
    # 새로운 시도
    # serializer는 조작불가이다.

    # serializer.data['title'] = '이상한제목'
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    # print(serializer.data['content'])
    return Response(serializer.data)
    # return JsonResponse({1:1})

# POST MAN 요청으로 비정상적인 접근을 시도했을 경우 어떻게 대처해야 하는가?
@api_view(['GET','POST'])
def like_review(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False

        else:
            review.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'like_count': review.like_users.count(),
        }
        return JsonResponse(context)

@api_view(['GET', 'POST'])
def get_reviews(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    reviews = Review.objects.filter(user_id=user.id)
    # reviews = get_list_or_404(Review, user_id=user.id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_review(request):
    review = request.data.get('new_review')
    user = get_object_or_404(get_user_model(), username=review["me"])
    # print(review)
    # print(user.id)
    reviews = Review.objects.filter(movie=review["movie_id"])
    # print(len(reviews))
    for i in range(len(reviews)):
        if user.id == list(reviews.values('user_id'))[i]["user_id"]:
    # if reviews and user.id == list(reviews.values('user_id'))[0]["user_id"]:
        # 이 아이디로 이 영화에 글을 썼음
        # 이미 이 아이디로 이 영화에 글을 썼잖아! 라고 보여줘야함
            new_id = reviews.values('id')[i]['id']
            already_writen = True
            return JsonResponse({'new_id': new_id, 'already_writen': already_writen, })
    new = Review(title=review['title'], rank=review['rank'], content=review['content'], movie_id=review['movie_id'], user_id=user.id)
    new.save()
    new_id = new.id
    already_writen = False
    # print(new_id)
    # return JsonResponse({1:1})
    return JsonResponse({'new_id': new_id, 'already_writen': already_writen, })

@api_view(['PUT','DELETE'])
def create_delete_comment(request, review_pk):
    if request.method == 'PUT':
        comment = Comment()
        comment.content = request.data.get('comment')
        comment.review_id = review_pk
        comment.user_id = request.data.get('me')
        comment.save()
    else:
        comment = Comment.objects.get(pk=review_pk)
        comment.delete()
    return Response({1:1})

@api_view(['POST'])
def get_comment(request, review_pk):
    comment_list = Comment.objects.filter(review_id=review_pk)
    serializer = CommentSerializer(comment_list, many=True)
    return Response(serializer.data)

@api_view(['PUT','DELETE'])
def update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        new_review = request.data['new_review']
        review.title = new_review['title']
        review.rank = new_review['rank']
        review.content = new_review['content']
        review.save()
        new_id = review.id
    #     print(serializer)
        return JsonResponse({'new_id': new_id})
    else:
        review.delete()
        return JsonResponse({1:1})

