from django.urls import path
from . import views
app_name="users"
urlpatterns = [
    path("all", views.user_list_view, name="user_list"),
    path("<slug:user_slug>", views.user_view, name="user_view"),
    path("<slug:user_slug>/follow", views.follow_view, name="follow"),
    path("<slug:user_slug>/unfollow", views.unfollow_view, name="unfollow"),
]
