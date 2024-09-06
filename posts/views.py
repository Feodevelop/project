from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from users.models import Profiles
from .form import PostForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def promotion(request, category_slug=None):
    categories = Category.objects.filter(parent__isnull=True)  # 상위 카테고리만 가져옴
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    # 각 게시글의 작성자 이름을 Profile에서 가져옴
    posts_with_author = []
    for post in posts:
        profile = Profiles.objects.get(user=post.user)  # User와 연결된 Profile 찾기
        posts_with_author.append({
            'post': post,
            'author_name': profile.name  # Profile에서 name 가져오기
        })

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('promotion')  # 적절한 URL로 리다이렉트
    else:
        form = PostForm()

    return render(request, 'promotion.html', {'posts': posts_with_author, 'categories': categories, 'form': form})

@login_required
def reports(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # 먼저 폼 데이터를 저장하지 않고 인스턴스를 반환합니다.
            post.user = request.user  # 현재 로그인된 사용자를 할당합니다.
            post.save()  # 이제 데이터를 데이터베이스에 저장합니다.
            return redirect('/posts/promotion/')  # 적절한 URL로 리다이렉트
    else:
        form = PostForm()

    return render(request, 'villagereport.html', {'form': form})


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Category.objects.filter(parent_id=category_id)
    subcategory_list = [('<option value="{}">{}</option>'.format(sub.id, sub.name)) for sub in subcategories]
    return JsonResponse(subcategory_list, safe=False)

def promotion_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'promotion_detail.html', {'post': post})

def notice(request):
    return render(request, 'notice.html')

def talk(request):
    return render(request, 'talk.html')
# Create your views here.
