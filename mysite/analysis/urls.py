"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'analysis'

urlpatterns = [
    # ex: /analysis/
    path('', views.index_analysis, name='index_analysis'),
    # # ex: /analysis/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /analysis/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /analysis/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
