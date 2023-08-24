from django.urls import path
from . import views
app_name="instaapp"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("grid", views.grid_view, name="grid"),
    path("post", views.post_view, name="post"),
    path("user", views.user_view, name="user")
]