from django.urls import path 
from .views import ApiView,UpdateCompanyView,CreateCompanyView,RetrieveCompanyView,UpdateCoursesView,CreateCoursesView,RetrieveCoursesView,UpdateMentorsView,CreateMentorsView,RetrieveMentorsView

urlpatterns = [
    path('',ApiView.as_view(),name='home_api'),
    path('update_company/<int:id>',UpdateCompanyView.as_view()),
    path('create_company/',CreateCompanyView.as_view()),
    path('retrive_company/<int:id>',RetrieveCompanyView.as_view()),
    path('update_course/<int:id>',UpdateCoursesView.as_view()),
    path('create_course/',CreateCoursesView.as_view()),
    path('retrive_course/<int:id>',RetrieveCoursesView.as_view()),
    path('update_mentor/<int:id>',UpdateMentorsView.as_view()),
    path('create_mentor/',CreateMentorsView.as_view()),
    path('retrive_mentor/<int:id>',RetrieveMentorsView.as_view()),
]
