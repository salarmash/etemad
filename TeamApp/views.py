from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Recruit, Category
from .serializers import TeamSerializer, RecruitSerializer, CategorySerializer


class TeamView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SingleView(APIView):
    def get(self, request, pk):
        instance = Team.objects.get(id=pk)
        serializer = TeamSerializer(instance=instance, context={'request': request}).data

        return Response(data=serializer, status=status.HTTP_200_OK)


class RecruitView(APIView):
    def get(self, request):
        recruit = Recruit.objects.all().last()
        data = RecruitSerializer(instance=recruit, context={"request": request}).data

        return Response(data=data, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(instance=category, many=True, context={'request': request}).data

        return Response(data=data, status=status.HTTP_200_OK)
