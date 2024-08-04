from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category, Project, Benefit
from .serializers import CategorySerializer, ProjectSerializer, BenefitSerializer


class AllProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        data = ProjectSerializer(instance=projects, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class ProjectView(APIView):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        data = ProjectSerializer(instance=project, context={'request': request}).data

        return Response(data=data, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(instance=category, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class BenefitView(APIView):
    def get(self, request):
        benefit = Benefit.objects.all().last()
        data = BenefitSerializer(instance=benefit, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
