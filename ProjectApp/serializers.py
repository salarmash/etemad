from rest_framework import serializers
from .models import Category, Project, Intro, Descriptions, Avatar, Gallery, Detail, Resume, Benefit, BenefitItem


class IntroSerializer(serializers.ModelSerializer):
    bgImage = serializers.SerializerMethodField()

    class Meta:
        model = Intro
        exclude = ("id", 'project')

    def get_bgImage(self, obj):
        request = self.context.get("request")
        if obj.bgImage:
            image_url = obj.bgImage.url
            return request.build_absolute_uri(image_url)


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptions
        exclude = ("id", "project")


class AvatarSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        exclude = ("id", "project")

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        exclude = ("id", "project")


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        exclude = ("id", "project")

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        exclude = ("id", "project")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("id",)


class ProjectSerializer(serializers.ModelSerializer):
    intro = IntroSerializer(read_only=True)
    description = DescriptionSerializer(read_only=True)
    avatar = AvatarSerializer(read_only=True)
    images = GallerySerializer(many=True, read_only=True)
    details = DetailSerializer(many=True, read_only=True)
    resume = ResumeSerializer(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class BenefitItemSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = BenefitItem
        exclude = ("id",)

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class BenefitSerializer(serializers.ModelSerializer):
    items = BenefitItemSerializer(many=True, read_only=True)

    class Meta:
        model = Benefit
        exclude = ("id",)
