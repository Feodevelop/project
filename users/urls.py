from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('signup/', views.signup, name="signup"),
    path('mypage/', views.mypage, name="mypage"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]