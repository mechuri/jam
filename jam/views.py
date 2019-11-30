from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .models import Project, Jam
from .forms import ProjectForm, JamForm, LoginForm, SignupForm
from django.contrib.auth.models import User
import pdb

# Create your views here.

def main(request):
    return render(request, 'main.html')


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


def show(request):
    request.POST.get('user')
    project = Project.objects.all()
    return render(request, 'show.html', {"project":project})


def createform(request, id):
    project = get_object_or_404(Project, pk=id)
    context = {
        'project': project,
        'no': no
    }
    
    if no == -1:
        return render(request, 'create_jam.html')
    else:
        return render(request, "create_jam.html", context)
    

def create_jam(request, id):
    project = get_object_or_404(Project, pk=id)
    context = {
        'project': project
    }
    if request.method == "POST":
        pdb.set_trace()
        jam = get_object_or_404(Jam, pk=id)
        jam.inst = request.POST['inst']
        jam.user = request.user
        jam.content = request.POST['content']
        jam.file = request.FILES['file']

        if request.POST['no'] == '-1':
                value = Jam.objects.aggregate(max_groupno=Max('groupno'))
                jam.groupno = value["max_groupno"]+1
                jam.save()
                
        else:
            jam2 = Jam.objects.get(id=request.POST['no'])
            Jam.objects.filter(orderno__gte=jam2.orderno+1).update(orderno=F('orderno')+1)
            jam.groupno = jam2.groupno
            jam.orderno = jam2.orderno+1
            jam.depth = jam2.depth+1
            jam.save()
        return redirect('jam:detail', project.id)
    return render(request, 'create_jam.html', context)



    

def detail(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'detail.html', {"project": project})

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = authenticate(
                username = username,
                password = password
            )
            
        if user:
            django_login(request, user)
            return redirect('jam:show')
        login_form.add_error(None, '아이디 또는 비밀번호를 확인해주십시오')
    else:
        login_form = LoginForm
    context = {
        'login_form': login_form,
    }
    
    return render(request, 'account/login.html', context)


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.signup()
            return redirect('acoounts:login')
    else:
        signup_form = SignupForm()
        
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'account/login.html', context)

    
