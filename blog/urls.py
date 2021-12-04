from django.urls import path
from .views import addPost, home, loginView, logoutView, postDetail,  postList, register

urlpatterns = [
    path("", home, name='home'),
    path("register/", register, name='register'),
    path("login/", loginView, name='login'),
    path("logout/", logoutView, name='logout'),
    path("newpost/", addPost, name='newpost'),
    path("posts/", postList, name='posts'),
    path("posts/<int:id>/", postDetail, name='post'),
]
