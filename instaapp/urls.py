from django.urls import path
from . import views
app_name="instaapp"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("grid", views.grid_view, name="grid"),
    path("posts/<slug:post_slug>", views.post_view, name="post"),
    path("posts/<slug:post_slug>/like", views.like_view, name="like_post"),
    path("posts/<slug:post_slug>/unlike", views.unlike_view, name="unlike_post"),
    path("posts/<slug>/edit", views.PostUpdateView.as_view(), name="edit_post"),
    path("create", views.create_post, name="create")
]