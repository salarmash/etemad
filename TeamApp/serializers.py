from rest_framework import serializers
from .models import Team, Info, Social, Avatar, Category, Recruit


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    info = InfoSerializer(many=True, read_only=True)
    social = SocialSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()
    fullImage = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

    def get_fullImage(self, obj):
        request = self.context.get("request")
        if obj.fullImage:
            fullImage_url = obj.fullImage.url
            return request.build_absolute_uri(fullImage_url)


class AvatarSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class RecruitSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Recruit
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")
