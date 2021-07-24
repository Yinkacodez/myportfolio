from django.shortcuts import render
from projects.models import Project


def index(request):

    projects = Project.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'index.html', context)

def project_detail(request):

        project = Project.objects.all()

        context = {

            'projects': project

        }

        return render(request, 'portfolio-details.html', context)

    