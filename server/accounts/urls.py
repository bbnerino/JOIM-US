from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

app_name = 'accounts'

urlpatterns = [
    # str 형식으로 요청이 올 경우, str 타입을 생략시키고 <username> 이라고 적어놓은 부분이 모두 잡아먹어서
    # api-token-auth 요청을 username 으로 인식해서 제대로 요청이 가지 않았었다. (3시간)
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('set_my_id/', views.set_my_id),
    path('getactorsforcheck/', views.get_actors_for_check),
    path('<int:user_pk>/getmyactors/', views.get_my_actors),
    path('<int:user_pk>/likethisactor/<int:actor_pk>/', views.like_this_actor),
    path('<username>/follow/', views.follow),
    # url 요청이 hong/like/ -> username/follow에 안걸리니까
    # 모두 묶어서 'hong/like' 라는 이름으로 views.profile 에 넘겨주나보다.
]
