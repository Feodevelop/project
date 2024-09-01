from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles
from django.contrib.auth.forms import AuthenticationForm

# 회원가입
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label="이메일")
    phonenum = forms.CharField(required=True, max_length=13, label="핸드폰 번호")
    name = forms.CharField(required=True, max_length=10, label="이름")

    class Meta:
        model = User
        fields = ('name', 'phonenum', 'username', 'email', 'password1', 'password2')
        labels = {
            'username': '아이디',
            'email': '이메일',
            'password1': '비밀번호',
            'password2': '비밀번호 확인'
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # 'usable_password' 필드 제거
        if 'usable_password' in self.fields:
            del self.fields['usable_password']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profiles.objects.create(
                user=user,
                phonenum=self.cleaned_data['phonenum'],
                name=self.cleaned_data['name']
            )
        return user
    
# 로그인
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디', max_length=254, required=True)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput, required=True)