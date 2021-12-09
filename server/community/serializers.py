from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):
    # 이 경우에는 USER에 대한 정보를 담고있기 때문에, Password와 같이 민감한 부분도 모두 노출시킬 수 있어서, depth=1을 사용하는 것은 위험하다.
    # 따라서 예를들어 like_users field를 조작하고 싶은 경우 아래와 같이 새로운 Serializer를 정의해서 사용하는 것이 좋다.
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('username',)
        
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # 1:N 일때는 N이 1에 대한 pk값을 모델에 가지고있기 때문에, 깊이를 하나 더 들어가서 나와 관계되어있는 모든 데이터를 표현시키도록 해주는 표현이 depth = 1 이다.
        # depth = 1

class ReviewSerializer2(serializers.ModelSerializer):
    class UserSerializer2(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('username',)

    like_users = UserSerializer2(many=True, read_only=True)
    user = UserSerializer2(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('username',)

    user = UserSerializer(read_only=True)

    content = serializers.CharField(
        min_length=2,
        max_length=200,
    )
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user',)