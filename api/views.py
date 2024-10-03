from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,RetrieveAPIView
from .serializers import CompanySerializer,MentorsSerializer,CoursesSerializer,CommentsSerializer
from myexam.models import Company,Mentors,Courses,Comments

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ApiView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        courses = Courses.objects.all()
        mentors = Mentors.objects.all()  # Получаем менторов
        company_serializer = CompanySerializer(companies, many=True)
        courses_serializer = CoursesSerializer(courses, many=True)
        mentors_serializer = MentorsSerializer(mentors, many=True)  # Сериализуем менторов
        
        return Response({
            'companies': company_serializer.data,
            'courses': courses_serializer.data,
            'mentors': mentors_serializer.data  # Добавляем менторов в ответ
        }, status=status.HTTP_200_OK)



class UpdateCompanyView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CreateCompanyView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class RetrieveCompanyView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UpdateCoursesView(UpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CompanySerializer

class CreateCoursesView(CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CompanySerializer

class RetrieveCoursesView(RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class UpdateMentorsView(UpdateAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorsSerializer

class CreateMentorsView(CreateAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorsSerializer

class RetrieveMentorsView(RetrieveAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorsSerializer