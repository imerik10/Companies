from myexam.models import Company,Mentors,Courses,Comments
from rest_framework.serializers import ModelSerializer

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class MentorsSerializer(ModelSerializer):
    class Meta:
        model = Mentors
        fields = '__all__'

class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
