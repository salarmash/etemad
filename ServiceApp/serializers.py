from rest_framework import serializers
from .models import Service, Description, Description2, DescriptionList, Gallery, SideBarContent, SideBarCounter, \
    SideBarItem, \
    FAQSection, FAQItem, VisionsSection, VisionItem, Contact, ContactPhone, ContactEmail, ContactAddress, AboutSection, \
    AboutList, Feature, FeatureItem, SideBar


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"


class Description2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Description2
        fields = "__all__"


class DescriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionList
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class ServiceSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(read_only=True)
    descriptions2 = Description2Serializer(read_only=True)
    listItems = DescriptionListSerializer(many=True, read_only=True)
    images = GallerySerializer(many=True, read_only=True)
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get("request")
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class SideBarContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBarContent
        fields = "__all__"


class SideBarCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBarCounter
        fields = "__all__"


class SideBarItemSerializer(serializers.ModelSerializer):
    contents = SideBarContentSerializer(many=True, read_only=True)

    class Meta:
        model = SideBarItem
        fields = "__all__"


class FAQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    faqItems = FAQItemSerializer(many=True, read_only=True)

    class Meta:
        model = FAQSection
        fields = "__all__"


class VisionItemSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = VisionItem
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get("request")
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class VisionSerializer(serializers.ModelSerializer):
    VItems = VisionItemSerializer(many=True, read_only=True)

    class Meta:
        model = VisionsSection
        fields = "__all__"


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPhone
        fields = "__all__"


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAddress
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = "__all__"


class AboutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutList
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    aboutLists = AboutListSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    avatar_image = serializers.SerializerMethodField()

    class Meta:
        model = AboutSection
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image_url:
            image_url_link = obj.image_url.url
            return request.build_absolute_uri(image_url_link)

    def get_avatar_image(self, obj):
        request = self.context.get("request")
        if obj.avatar_image:
            avatar_image_url = obj.avatar_image.url
            return request.build_absolute_uri(avatar_image_url)


class FeatureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureItem
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    featureItems = FeatureItemSerializer(many=True, read_only=True)

    class Meta:
        model = Feature
        fields = "__all__"
