from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hero, About, Idea, Service, Advantage, HowWeWork, Core
from .serializers import HeroSerializer, AboutSerializer, IdeaSerializer, ServiceSerializer, AdvantageSerializer, \
    HowWeWorkSerializer, CoreSerializer
from rest_framework import status


class HeroView(APIView):
    def get(self, request):
        hero = Hero.objects.all().last()
        data = HeroSerializer(instance=hero, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutView(APIView):
    def get(self, request):
        about = About.objects.all().last()
        data = AboutSerializer(instance=about, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class IdeaView(APIView):
    def get(self, request):
        idea = Idea.objects.all().last()
        data = IdeaSerializer(instance=idea, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class ServiceView(APIView):
    def get(self, request):
        service = Service.objects.all().last()
        data = ServiceSerializer(instance=service, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class AdvantageView(APIView):
    def get(self, request):
        advantage = Advantage.objects.all().last()
        data = AdvantageSerializer(instance=advantage).data
        return Response(data=data, status=status.HTTP_200_OK)


class HowWeWorkView(APIView):
    def get(self, request):
        how_we_work = HowWeWork.objects.all().last()
        data = HowWeWorkSerializer(instance=how_we_work, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class CoreView(APIView):
    def get(self, request):
        core = Core.objects.all().last()
        data = CoreSerializer(instance=core, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
