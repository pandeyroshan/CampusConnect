from django.contrib import admin
from django.urls import path
from CamCon import views as CamCon_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CamCon_views.index, name='home'),
    path('chat/',CamCon_views.chat, name='chat'),
    path('login/', auth_views.LoginView.as_view(template_name='CamCon/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='CamCon/logout.html'), name='logout'),
]