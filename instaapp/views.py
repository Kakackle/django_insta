from django.shortcuts import render
from instaapp.models import Post, Comment, Tag
from django.contrib.auth.models import User
from users.models import UserProfile, Following
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home_view(request):
    # posty z wykluczeniem postow wlasnych autora
    posts_all = Post.objects.exclude(author=request.user.id)
    if (request.user.is_authenticated):
        followed_users_pks = list(request.user.followed.all()\
                                .values_list('followed_user', flat=True))
        followed_users = User.objects.filter(pk__in=followed_users_pks)
    else:
        followed_users = []
    # print('followed: ', followed_users)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_all, 4)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        "posts": posts,
        "user": request.user,
        "followed_users": followed_users
    }
    return render(request, "instaapp/home.django-html", context)

def grid_view(request):
    return render(request, "instaapp/grid.django-html")

def post_view(request):
    return render(request, "instaapp/post.django-html")