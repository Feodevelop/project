from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from .form import SignupForm
from .form import LoginForm
from django.contrib.auth import logout

def home(request):
    # 홈 페이지 접근 시 로그아웃
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')  # 홈 페이지로 리디렉션

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'signup.html', {'form':form})
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('main'))
        else:
            return render(request, 'signup.html', {'form':form})

def mypage(request):
    return render(request, 'mypage.html')

# 로그인 화면 
def loginPage(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html')
    elif request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '로그인 성공')
                return redirect('main')
            else:
                messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
        else:
            # 폼이 유효하지 않을 때의 처리를 추가합니다.
            messages.error(request, '아이디와 비밀번호를 정확히 입력해주세요.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})