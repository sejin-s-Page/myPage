from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    # path('new_post/', views.post_create, name='post-create'), # login 기능 추가 시 주석 풀기
]
