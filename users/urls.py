from django.urls import path
from . import views
app_name="accounts"
urlpatterns = [
    path("users/<slug:user_slug>", views.user_view, name="user_view"),
]
