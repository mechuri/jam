from django import forms
from django.contrib.auth import get_user_model

from .models import Project, Jam

User = get_user_model()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'content',
            'inst',
            'file',
        ]
        

class JamForm(forms.ModelForm):
    class Meta:
        model = Jam
        fields = [
            'content',
            'inst',
            'file',
        ]
        
        
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    
class SignupForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다')
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다')
        return password2
    
    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )
