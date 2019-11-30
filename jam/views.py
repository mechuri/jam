from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .models import Project, Jam
from .forms import ProjectForm, JamForm, LoginForm, SignupForm
from django.contrib.auth.models import User
import pdb

# Create your views here.

def main(request):
    request.POST.get('user')
    project = Project.objects.all()
    return render(request, 'main.html', {"project":project})



def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('main')
    return render(request, 'create_project.html', {'form': form})


def create_jam(request, id):
    form = JamForm()
    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        form = JamForm(request.POST, request.FILES)
        if form.is_valid():
            jam = form.save(commit=False)
            jam.project = project
            jam.user = request.user
            jam.save()
            return redirect('jam:detail', project.id)

    return render(request, 'create_jam.html', {'form': form, "id": id})
    
    
def detail(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'detail.html', {"project": project})

