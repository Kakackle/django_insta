from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from users.models import UserProfile, Following
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def user_view(request, user_slug):
    user = User.objects.get(username=user_slug)

    if (request.user.is_authenticated):
        followed_users_pks = list(request.user.followed.all()\
                                .values_list('followed_user', flat=True))
        followed_users = User.objects.filter(pk__in=followed_users_pks)
    else:
        followed_users = []

    context = {
        'user' : user,
        "followed_users": followed_users,
    }
    return render(request, "users/user_view.django-html", context)

def user_list_view(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "users/user_list.django-html", context)

@login_required()
def follow_view(request, user_slug):
    print('user_slug: ', user_slug)
    print('request user: ', request.user.username)
    try:
        user = get_object_or_404(User, username=user_slug)
    except Http404:
        return redirect('users:user_list')
    followed_users_pks = list(request.user.followed.all()\
                              .values_list('followed_user', flat=True))
    followed_users = User.objects.filter(pk__in=followed_users_pks)
    if request.POST:
        if user not in followed_users:
            Following.objects.create(followed_user=user,
                                     following_user=request.user,
                                     date_followed=timezone.now())
            user.profile.followed_by_count += 1
            user.profile.save()
            request.user.profile.followed_count += 1
            request.user.profile.save()

    #aktualizacja
    followed_users_pks = list(request.user.followed.all()\
                              .values_list('followed_user', flat=True))
    followed_users = User.objects.filter(pk__in=followed_users_pks)
    context = {
        "user": user
    }
    if user not in followed_users:
        return render(request, "users/follow.django-html", context)
    else:
        return render(request, "users/unfollow.django-html", context)
    # return redirect('users:user_view', user_slug=user.username)

@login_required()
def unfollow_view(request, user_slug):
    print('user_slug: ', user_slug)
    print('request user: ', request.user.username)
    try:
        user = get_object_or_404(User, username=user_slug)
    except Http404:
        return redirect('users:user_list')
    followed_users_pks = list(request.user.followed.all()\
                              .values_list('followed_user', flat=True))
    followed_users = User.objects.filter(pk__in=followed_users_pks)
    if request.POST:
        if user in followed_users:
            following = Following.objects.get(followed_user=user.pk)
            following.delete()
            user.profile.followed_by_count -= 1
            user.profile.save()
            request.user.profile.followed_count -= 1
            request.user.profile.save()

    followed_users_pks = list(request.user.followed.all()\
                              .values_list('followed_user', flat=True))
    followed_users = User.objects.filter(pk__in=followed_users_pks)
    
    context = {
        "user": user
    }
    if user in followed_users:
        return render(request, "users/unfollow.django-html", context)
    else:
        return render(request, "users/follow.django-html", context)
    # return redirect('users:user_view', user_slug=user.username)
            