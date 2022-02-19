from django.shortcuts import render

# Create your views here.

#  Form이 HTML form을 생성하는 것에 반해, Serializer는 JSON 문자열을 생성
# class Class_name(APIView):
	# def method_name(self, request, format=None):
    # 	# 해당 HTTP method를 어떻게 동작시키고 처리할지 개발자가 정의!

# views.py는 Blog 전체 목록을 보여주는 역할을 하는 BlogList 클래스와,

# Blog 객체의 detail을 보여주는 BlogDetail 클래스 두 개를 선언하였습니다.

# 데이터 처리
from .models import Blog
from .serializers import BlogSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Blog의 목록을 보여주는 역할
class BlogList(APIView):
    # Blog list를 보여줄 때
    def get(self, request):
        blogs = Blog.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    # 새로운 Blog 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Blog의 detail을 보여주는 역할
class BlogDetail(APIView):
    # Blog 객체 가져오기
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
    
    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    # Blog 수정하기
    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


