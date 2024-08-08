from rest_framework import serializers
from .models import Category, Tag, Post, Author, Comment, SocialGroupSidebar, SocialSideBar, EmailSidebar


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Author
        exclude = ("id",)

    def get_avatar(self, obj):
        request = self.context.get('request')
        if obj.avatar:
            avatar_url = obj.avatar.url
            return request.build_absolute_uri(avatar_url)


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class CommentSerializer(serializers.ModelSerializer):
    # post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class SocialSideBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialSideBar
        fields = "__all__"


class EmailSideBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSidebar
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):
    email = EmailSideBarSerializer(many=True, read_only=True)
    socials = SocialSideBarSerializer(many=True, read_only=True)

    class Meta:
        model = SocialGroupSidebar
        fields = "__all__"
