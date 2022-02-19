from .models import Blogviewsets
from .serializers import BlogSerializerviewsets
from rest_framework import viewsets

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogviewsets.objects.all()
    serializer_class = BlogSerializerviewsets
