from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Post
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=["get"], detail=True)
    def like(self, request, **kwargs):
        if Post.objects.get(id=kwargs.get("pk")).liked_users.contains(request.user):
            return Response({"detail": "Вы уже поставили лайк"})
        else:
            Post.objects.get(id=kwargs.get("pk")).liked_users.add(request.user)
            return Response({"detail": "Вы поставили лайк"})

    @action(methods=["get"], detail=True)
    def unlike(self, request, **kwargs):
        if Post.objects.get(id=kwargs.get("pk")).liked_users.contains(request.user):
            return Response({"detail": "Вы убрали лайк"})
        else:
            return Response({"detail": "Вы не ставили лайк"})
