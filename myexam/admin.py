from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Company)
admin.site.register(Mentors)
admin.site.register(Comments)


@admin.register(Courses)
class Coursesclass(admin.ModelAdmin):
    list_display = ['course_title','course_price','course_company','course_mentor','show_image']
    list_display_links = ['course_title','course_mentor']
    list_filter = ['course_company','course_mentor']
    list_editable =['course_price']

    def show_image(self,photo):
        if photo.course_poster:
            return mark_safe(f"<img src='{photo.course_poster.url}' width=60 >")
        return None
    show_image.__name__='Photo'


