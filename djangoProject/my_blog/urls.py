from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("news/", views.news, name="news"),
    path("contact/", views.contact, name="contact")
]
