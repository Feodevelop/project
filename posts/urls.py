from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('promotion/', views.promotion, name="promotion"),
    path('notice/', views.notice, name="notice"),
    path('talk/', views.talk, name="talk"),
    path('reports/', views.reports, name='reports'),
    path('category/<slug:category_slug>/', views.promotion, name='promotion_by_category'),
    path('post/<int:post_id>/', views.promotion_detail, name='promotion_detail'),
    path('get-subcategories/', views.get_subcategories, name='get_subcategories'),
]