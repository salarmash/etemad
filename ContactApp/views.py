from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer, ContactFormSerializer


class ContactView(APIView):
    def get(self, request):
        contact = Contact.objects.all().last()
        data = ContactSerializer(instance=contact).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "درخواست با موفقیت ثبت شذ",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": 400,
            "message": "مشکلی پیش آمده",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
