from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]