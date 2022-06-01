from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from api.models import Post


class PostSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField("likes_count")
    author_username = ReadOnlyField(source="author.username")

    def likes_count(self, obj):
        return obj.liked_users.count()

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "author_username",
            "title",
            "body",
            "like",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("author",)
