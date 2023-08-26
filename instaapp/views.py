from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.http import HttpResponseRedirect
from instaapp.models import Post, Comment, Tag
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import UserProfile, Following
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home_view(request):
    # posty z wykluczeniem postow wlasnych autora
    posts_all = Post.objects.exclude(author=request.user.id).order_by("-date_posted")
    if (request.user.is_authenticated):
        followed_users_pks = list(request.user.followed.all()\
                                .values_list('followed_user', flat=True))
        followed_users = User.objects.filter(pk__in=followed_users_pks)
    else:
        followed_users = []
    # print('followed: ', followed_users)

    followed = request.GET.get('followed', False)
    # print('followed: ', followed)

    if followed and followed_users:
        posts_all = posts_all.filter(author__in=followed_users)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_all, 4)

    liked_posts = request.user.liked_posts.all()
    print('liked_posts ',liked_posts)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        "posts": posts,
        "user": request.user,
        "followed_users": followed_users,
        "followed": followed,
        "page": page
    }
    return render(request, "instaapp/home.django-html", context)

def grid_view(request):
    # posty z wykluczeniem postow wlasnych autora
    posts_all = Post.objects.exclude(author=request.user.id).order_by("-date_posted")
    
    # jakas filtracja itepe
    if (request.user.is_authenticated):
        followed_users_pks = list(request.user.followed.all()\
                                .values_list('followed_user', flat=True))
        followed_users = User.objects.filter(pk__in=followed_users_pks)
        #
        liked_posts = request.user.liked_posts
    else:
        followed_users = []
    # print('followed: ', followed_users)

    followed = request.GET.get('followed', False)
    if followed and followed_users:
        posts_all = posts_all.filter(author__in=followed_users)

    liked = request.GET.get('liked', False)
    if liked and liked_posts:
        posts_all = liked_posts

    search = request.GET.get('search', '')
    # print('search', search)

    # filtracja po tresci
    posts_by_desc = posts_all.filter(description__contains=search)

    #filtracja po tagach
    posts_by_tag = posts_all.filter(tags__name=search)

    posts = (posts_by_desc | posts_by_tag).distinct()

    context = {"posts": posts,
               "followed": followed,
               "liked": liked}
    return render(request, "instaapp/grid.django-html", context)

@login_required()
def like_view(request, post_slug):
    try:
        post = get_object_or_404(Post, slug=post_slug)
    except Http404:
        return redirect('instaapp:home')
    page = 1
    if request.POST:
        if request.user not in post.liked_by.all():
            post.liked_by.add(request.user)
            post.like_count += 1
            post.save()
            request.user.liked_posts.add(post)
            request.user.save()
        
    page = request.POST.get("page", 1)

    return HttpResponseRedirect('/?page={}'.format(page))
    # return redirect(request.META.get('HTTP_REFERER', 'instaapp:grid'))

def unlike_view(request, post_slug):
    try:
        post = get_object_or_404(Post, slug=post_slug)
    except Http404:
        return redirect('instaapp:home')
    page = 1
    if request.POST:
            if request.user in post.liked_by.all():
                post.liked_by.remove(request.user)
                post.like_count -= 1
                post.save()
                request.user.liked_posts.remove(post)
                request.user.save()
    page = request.POST.get("page", 1)

    return HttpResponseRedirect('/?page={}'.format(page))

    # return redirect(request.META.get('HTTP_REFERER', 'instaapp:home'))

def post_view(request, post_slug):
    try:
        post = get_object_or_404(Post, slug=post_slug)
    except Http404:
        return redirect('instaapp:home')
    
    if (request.user.is_authenticated):
        followed_users_pks = list(request.user.followed.all()\
                                .values_list('followed_user', flat=True))
        followed_users = User.objects.filter(pk__in=followed_users_pks)
    else:
        followed_users = []

    comments = post.comments.all()

    page = request.GET.get('comment_page', 1)
    paginator = Paginator(comments, 4)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    context = {"post": post,
               "user": request.user,
               "followed_users": followed_users,
               "comments": comments}

    return render(request, "instaapp/post.django-html", context)