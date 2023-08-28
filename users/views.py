from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfile, Following

# Create your views here.

def user_view(request, user_slug):
    user = User.objects.get(username=user_slug)
    context = {
        'user' : user
    }
    return render(request, "users/user_view.django-html", context)

def user_list_view(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "users/user_list.django-html", context)