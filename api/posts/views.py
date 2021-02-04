from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        if self.action == 'create':
            print('post', self.request.data)
            return PostCreateSerializer
        return PostSerializer