from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'project'

urlpatterns =[
    path('blog/', views.BlogList.as_view(), name='bloglist' ),
    path('blog/<int:pk>/', views.BlogDetail.as_view(), name='blogdetail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


