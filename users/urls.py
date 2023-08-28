from django.urls import path
from . import views
app_name="users"
urlpatterns = [
    path("all", views.user_list_view, name="user_list"),
    path("<slug:user_slug>", views.user_view, name="user_view"),
]
