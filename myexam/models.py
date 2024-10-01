from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    company_title = models.CharField(max_length=255,verbose_name='Company title')
    company_description = models.TextField(verbose_name='Description')
    company_logo = models.ImageField(upload_to='media',verbose_name='Company logo')



    class Meta:
        verbose_name='Company'
        verbose_name_plural='Companies'
    
    def __str__(self):
        return self.company_title

class Mentors(models.Model):
    mentor_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mentor_name = models.CharField(max_length=255,verbose_name="Mentor's full name")
    mentor_description = models.TextField(verbose_name='Description')
    mentor_photo = models.ImageField(upload_to='media',verbose_name="Mentor's photo (optional)",null=True,blank=True)

    class Meta:
        verbose_name='Mentor'
        verbose_name_plural='Mentors'
    
    def __str__(self):
        return self.mentor_name

class Courses(models.Model):
    course_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    course_mentor = models.ForeignKey(Mentors,on_delete=models.CASCADE)
    course_title = models.CharField(max_length=255,verbose_name='Course title')
    course_description = models.TextField(verbose_name='Description')
    course_price = models.IntegerField(verbose_name='Course price')
    course_date = models.DateField(verbose_name='Course Date')
    count_of_lessons = models.IntegerField(verbose_name='Count of lessons')
    course_poster = models.ImageField(upload_to='media',verbose_name='Course poster')


    class Meta:
        verbose_name='Course'
        verbose_name_plural='Courses'
     
    def __str__(self):
        return self.course_title




class Comments(models.Model):
    text = models.TextField(verbose_name='Comment')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Comment published date')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text
