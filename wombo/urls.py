"""wombo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from wombo import views as wombo_views
from polls import views as poll_views

router = routers.DefaultRouter()
router.register(r'users', wombo_views.UserViewSet)
router.register(r'groups', wombo_views.GroupViewSet)

v2_router = routers.DefaultRouter()
v2_router.register(r'questions', poll_views.QuestionViewSet)
v2_router.register(r'tags', poll_views.TagViewSet)
v2_router.register(r'choices', poll_views.ChoiceViewSet)

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('v2/', include(v2_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
