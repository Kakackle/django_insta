from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "instaapp/home.django-html")

def grid_view(request):
    return render(request, "instaapp/grid.django-html")

def post_view(request):
    return render(request, "instaapp/post.django-html")

def user_view(request):
    return render(request, "instaapp/user_view.django-html")