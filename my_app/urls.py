from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),

    path('', views.home, name="home"),
    path('about_me/', views.about_me, name="about_me"),
    path('room/<str:pk>/', views.room, name="room")
]