from rest_framework import serializers
from .models import Contact, ContactPhone, ContactAddress, ContactEmail, ContactForm


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


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"
