from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    project_objects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':project_objects})