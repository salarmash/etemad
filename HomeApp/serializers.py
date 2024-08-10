from rest_framework import serializers
from .models import Hero, HeroItem, About, Avatar, AboutItems, Idea, IdeaItem, Service, ServiceItem, Advantage, \
    AdvantageItem, HowWeWork, WorkItem, Core, CoreItem


class HeroItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = HeroItem
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class HeroSerializer(serializers.ModelSerializer):
    images = HeroItemSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = "__all__"


class AvatarSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class AboutItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutItems
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    avatar = AvatarSerializer(read_only=True)
    aboutItems = AboutItemsSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class IdeaItemSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = IdeaItem
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class IdeaSerializer(serializers.ModelSerializer):
    ideaItems = IdeaItemSerializer(many=True, read_only=True)

    class Meta:
        model = Idea
        fields = "__all__"


class ServiceItemSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = ServiceItem
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class ServiceSerializer(serializers.ModelSerializer):
    serviceItems = ServiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"


class AdvantageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantageItem
        fields = "__all__"


class AdvantageSerializer(serializers.ModelSerializer):
    advantageItems = AdvantageItemSerializer(many=True, read_only=True)

    class Meta:
        model = Advantage
        fields = "__all__"


class WorkItemSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = WorkItem
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class HowWeWorkSerializer(serializers.ModelSerializer):
    workItems = WorkItemSerializer(many=True, read_only=True)

    class Meta:
        model = HowWeWork
        fields = "__all__"


class CoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreItem
        fields = "__all__"


class CoreSerializer(serializers.ModelSerializer):
    coreItems = CoreItemSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Core
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
