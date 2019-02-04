from django.urls import path, re_path

# 2차 url
from .views import *

# url 이름을 가지고 패턴을 찾고자할 때 namespace를 사용하려면 app_name이 필수!
app_name = 'bookmark'

urlpatterns = [
    # list, write, update, delete
    # 함수형뷰 : 함수이름만
    # 클래스형뷰 : 클래스이름.as_view()

    path('', BookmarkListView.as_view(), name='list'),
    path('write/', BookmarkCreateView.as_view(), name='write'),
    # <1:2> : 1. data type, 2. data name
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    # re_path(regexp,,),
    # url(regexp,?,?)
]