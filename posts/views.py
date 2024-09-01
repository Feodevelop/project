from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .form import PostForm

def promotion(request, category_slug=None):
    categories = Category.objects.filter(parent__isnull=True)  # 상위 카테고리만 가져옴

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('promotion')  # 적절한 URL로 리다이렉트
    else:
        form = PostForm()
    
    return render(request, 'promotion.html', {'posts': posts, 'categories': categories, 'form': form})

def reports(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('promotion')  # 폼 저장 후 promotion 페이지로 리다이렉트
    else:
        form = PostForm()  # GET 요청 시 빈 폼을 생성

    return render(request, 'villagereport.html', {'form': form})


def promotion_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'promotion_detail.html', {'post': post})

def notice(request):
    return render(request, 'notice.html')

def talk(request):
    return render(request, 'talk.html')
# Create your views here.
