from rest_framework import serializers
from .models import Award, AwardItems, TestItems, Testimonial, ServiceItem, Service, Contact, Signature, Company, \
    Company2, CompanyImage, Company2Image, Process, Partner, AboutExtra, AllProcess, Group


class AwardItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = AwardItems
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class AwardSerializer(serializers.ModelSerializer):
    items = AwardItemSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Award
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class TestItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = TestItems
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class TestimonialSerializer(serializers.ModelSerializer):
    testItems = TestItemSerializer(many=True, read_only=True)

    class Meta:
        model = Testimonial
        fields = "__all__"


class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    serviceItems = ServiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = "__all__"


class CompanyImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CompanyImage
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class CompanySerializer(serializers.ModelSerializer):
    signature = SignatureSerializer(read_only=True)
    images = CompanyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class Company2ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Company2Image
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class Company2Serializer(serializers.ModelSerializer):
    images = Company2ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Company2
        fields = "__all__"


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'title', 'image']


class AboutExtraSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(many=True, read_only=True)

    class Meta:
        model = AboutExtra
        fields = ['id', 'name', 'partner']


class GroupSerializer(serializers.ModelSerializer):
    process = ProcessSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = "__all__"


class AllProcessSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = AllProcess
        fields = "__all__"
