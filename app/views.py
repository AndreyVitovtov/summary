from django.shortcuts import render

from .models import PersonalInformation, About, Avatar, Education, Experience, Skills, Portfolio


# Create your views here.
def home(request):
    return render(request, 'app/home.html', {
        'personal_info': PersonalInformation.objects.first(),
        'about': About.objects.first(),
        'avatar': Avatar.objects.first(),
        'educations': Education.objects.all(),
        'experience': Experience.objects.all(),
        'portfolio': Portfolio.objects.all(),
        'skills': Skills.objects.all()
    })
