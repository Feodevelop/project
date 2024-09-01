from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    path('promotion/', views.promotion, name="promotion"),
    path('notice/', views.notice, name="notice"),
    path('talk/', views.talk, name="talk"),
    path('reports/', views.reports, name='reports'),
    path('category/<slug:category_slug>/', views.promotion, name='promotion_by_category'),
    path('post/<int:post_id>/', views.promotion_detail, name='promotion_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)