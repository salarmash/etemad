from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category, Tag, Author, Post, Comment, SocialGroupSidebar
from .serializers import CategorySerializer, TagSerializer, AuthorSerializer, PostSerializer, CommentSerializer, \
    SocialSerializer
from rest_framework.pagination import PageNumberPagination


class AllPostView(APIView):
    def get(self, request):
        articles = Post.objects.all()
        paginator = PageNumberPagination()
        post = paginator.paginate_queryset(queryset=articles, request=request)
        data = {}
        data['posts'] = PostSerializer(post, many=True, context={'request': request}).data
        data['total'] = articles.count()
        data['next'] = paginator.get_next_link()
        data['previous'] = paginator.get_previous_link()
        data['count_per_page'] = len(post)

        return Response(data=data, status=status.HTTP_200_OK)


class SinglePost(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        comment = Comment.objects.filter(post=post)
        data = {}
        data['posts'] = PostSerializer(post, context={'request': request}).data
        data['comment'] = CommentSerializer(comment, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response({
                "status": 200,
                "message": "نظر با موفقیت ثبت شذ",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": 400,
            "message": "مشکلی پیش آمده",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class AllCategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        data = CategorySerializer(instance=category, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleCategoryView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        post = Post.objects.filter(categories=category)

        data = {}

        data['posts'] = PostSerializer(post, many=True, context={'request': request}).data
        data['category'] = CategorySerializer(instance=category).data
        return Response(data=data, status=status.HTTP_200_OK)


class AllTagView(APIView):
    def get(self, request):
        tag = Tag.objects.all()
        data = TagSerializer(instance=tag, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleTagView(APIView):
    def get(self, request, pk):
        tag = Tag.objects.get(id=pk)
        post = Post.objects.filter(tag=tag)
        data = {}
        data['posts'] = PostSerializer(post, many=True, context={'request': request}).data
        data['tag'] = TagSerializer(tag).data
        return Response(data=data, status=status.HTTP_200_OK)


class PopularView(APIView):
    def get(self, request):
        articles = Post.objects.filter(popular=True).last()
        data = PostSerializer(instance=articles, context={'request': request}).data

        return Response(data=data, status=status.HTTP_200_OK)


class AllAuthorView(APIView):
    def get(self, request):
        author = Author.objects.all()
        data = AuthorSerializer(author, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleAuthorView(APIView):
    def get(self, request, pk):
        author = Author.objects.get(id=pk)
        post = Post.objects.filter(author=author)
        data = {}
        data['posts'] = PostSerializer(instance=post, many=True, context={'request': request}).data
        data['author'] = AuthorSerializer(instance=author, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class RecentView(APIView):
    def get(self, request):
        articles = Post.objects.all()[:4]
        data = PostSerializer(instance=articles, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class SocialView(APIView):
    def get(self, request):
        instance = SocialGroupSidebar.objects.all().last()
        data = SocialSerializer(instance=instance).data
        return Response(data=data, status=status.HTTP_200_OK)


class WithoutPagination(APIView):
    def get(self, request):
        post = Post.objects.all()
        data = PostSerializer(post, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
