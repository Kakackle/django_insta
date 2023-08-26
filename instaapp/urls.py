from django.urls import path
from . import views
app_name="instaapp"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("grid", views.grid_view, name="grid"),
    path("posts/<slug:post_slug>", views.post_view, name="post"),
]