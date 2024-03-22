from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("character", views.character, name="character"),
    path("counter", views.counter, name="counter"),
    path("sucessful", views.sucessful, name="sucessful"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("post/<str:pk>", views.post, name="post"),
    path("login", views.login, name="login"),
    # path("search", views.search, name="search"),
    path("character/<str:pk>", views.character, name="character"),
]
