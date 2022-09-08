from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('loggedin', views.loggedin, name="logged_in"),
    path("logout", views.logout_request, name= "logout"),
    path("forgot", views.forgot_request, name= "forgot"),
    path("reset", views.resetdone, name= "reset"),
]
