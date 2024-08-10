from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AwardSerializer, TestimonialSerializer, ServiceSerializer, ContactSerializer, \
    CompanySerializer, Company2Serializer, PartnerSerializer, \
    AllProcessSerializer
from .models import Award, Testimonial, Service, Contact, Company, Company2, Partner, AllProcess
from rest_framework import status


class AboutView(APIView):
    def get(self, request):
        award = Award.objects.all().last()
        testimonial = Testimonial.objects.all().last()
        service = Service.objects.all().last()
        contact = Contact.objects.all().last()
        company = Company.objects.all().last()
        company2 = Company2.objects.all().last()

        data = {}
        if award:
            data["award"] = AwardSerializer(instance=award, context={"request": request}).data
        if testimonial:
            data["testimonial"] = TestimonialSerializer(instance=testimonial, context={"request": request}).data
        if service:
            data["services"] = ServiceSerializer(instance=service).data
        if contact:
            data["contactInfo"] = ContactSerializer(instance=contact).data
        if company:
            data["company"] = CompanySerializer(instance=company, context={"request": request}).data

        if company2:
            data["company2"] = Company2Serializer(instance=company2, context={"request": request}).data

        print(data)
        return Response(data=data, status=status.HTTP_200_OK)


class ProcessView(APIView):
    def get(self, request):
        process = AllProcess.objects.all().last()
        data = AllProcessSerializer(instance=process).data

        return Response(data=data, status=status.HTTP_200_OK)


class PartnerView(APIView):
    def get(self, request):
        partner = Partner.objects.all()
        data = PartnerSerializer(instance=partner, many=True, context={"request": request}).data

        return Response(data=data, status=status.HTTP_200_OK)
