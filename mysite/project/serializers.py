# serializer.py

# serializer.py는 project라는 앱 폴더 내부에 별도로 만들어주었습니다.

# 해당 파일에서는 주어진 데이터를 직렬화하는 역할을 한다고 생각하면 됩니다.

# 저는 fields를 '__all__'로 설정하였기 때문에 model의 title과 body를 모두 직렬화할 수 있었습니다.

# 필요에 따라서는 fields = ['title'] 등과 같이 model의 일부만 설정할 수도 있습니다.

from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'