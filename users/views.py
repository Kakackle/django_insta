from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfile, Following

# Create your views here.

def user_view(request, user_slug):
    user = User.objects.get(slug=user_slug)
    context = {
        'user' : user
    }
    return render(request, "accounts/user_view.django-html", context)
