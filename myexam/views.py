from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from . import models,forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    companyyy = models.Company.objects.all()
    return render(request,'home.html',{'companyyy':companyyy})


def product_detail(request,id):
    company = get_object_or_404(models.Company,id=id)
    comments = models.Comments.objects.filter(company=company)
    courses = models.Courses.objects.filter(course_company=company)
    if request.method=='POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.company = company
            new_comment.username = request.user
            new_comment.save()
            return redirect('detail',id=company.id)
    else:
        comment_form = forms.CommentForm()
    return render(request,'detail.html',{
            'company':company,
            'comments':comments,
            'comment_form':comment_form,
            'courses': courses,
        })
def course_detail(request, id):
    course = get_object_or_404(models.Courses, id=id)
    mentor = course.course_mentor
    return render(request, 'course_detail.html', {'course': course,'mentor': mentor})

def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'reg.html',{'form':form})

def signin(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')