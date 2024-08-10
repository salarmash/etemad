from .models import Service, SideBarItem, FAQSection, VisionsSection, Contact, AboutSection, Feature, SideBarCounter
from .serializers import ServiceSerializer, SideBarItemSerializer, FAQSerializer, VisionSerializer, ContactSerializer, \
    AboutSerializer, FeatureSerializer, SideBarCounterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ServiceView(APIView):
    def get(self, request):
        service = Service.objects.all()

        data = ServiceSerializer(instance=service, many=True, context={'request': request}).data

        return Response(data=data, status=status.HTTP_200_OK)


class SingService(APIView):
    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        data = ServiceSerializer(instance=service, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class FAQView(APIView):
    def get(self, request):
        faq = FAQSection.objects.all().last()
        data = FAQSerializer(instance=faq).data
        return Response(data=data, status=status.HTTP_200_OK)


class VisionView(APIView):
    def get(self, request):
        vision = VisionsSection.objects.all().last()
        data = VisionSerializer(instance=vision, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class SidebarView(APIView):
    def get(self, request):
        sidebar = SideBarItem.objects.all()
        data = SideBarItemSerializer(instance=sidebar, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class Counter(APIView):
    def get(self,request):
        counter = SideBarCounter.objects.all().last()
        data = SideBarCounterSerializer(instance=counter).data
        return Response(data=data, status=status.HTTP_200_OK)


class ContactView(APIView):
    def get(self, request):
        contact = Contact.objects.all().last()
        data = ContactSerializer(instance=contact).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutView(APIView):
    def get(self, request):
        about = AboutSection.objects.all().last()
        data = AboutSerializer(instance=about, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class FeatureView(APIView):
    def get(self, request):
        feature = Feature.objects.all()
        data = FeatureSerializer(instance=feature, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
