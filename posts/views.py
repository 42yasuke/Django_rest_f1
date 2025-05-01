from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post
from .serializers import PostSerializer
from .permissions import UpdateOwnProfile

class PostViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (
        UpdateOwnProfile,
        IsAuthenticatedOrReadOnly,
    )
	queryset = Post.objects.all()

class UserLoginApiView(ObtainAuthToken):
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES