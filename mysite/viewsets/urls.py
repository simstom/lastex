from django.urls import path
from .views import BlogViewSet

# Blog 목록 보여주기
blog_list = BlogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Blog detail 보여주기 + 수정 + 삭제
blog_detail = BlogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

app_name = 'viewsets'

urlpatterns =[
    path('blogviewsets/', blog_list, name = 'blogviewsetslist'),
    path('blogviewsets/<int:pk>/', blog_detail, name = 'blogviewsetsdetail'),
]