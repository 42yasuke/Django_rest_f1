from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserLoginApiView

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('login/', UserLoginApiView.as_view()),
]