from django.urls import path
from . import views


app_name = 'community'


urlpatterns = [
    path('',views.review_index,name='review_index'),
    path('create_review/', views.create_review),
    path('create_review/update_delete/<int:review_pk>/', views.update_delete),
    path('create_delete_comment/<int:review_pk>/', views.create_delete_comment),
    path('get_comment/<int:review_pk>/', views.get_comment),
    path('<int:review_pk>/like_review/', views.like_review),
    path('<username>/get_reviews/', views.get_reviews),
    path('<int:review_pk>/', views.detail_review),

]