import signup
from django.urls import path, include
from . import views
from .views import signin

urlpatterns= [
    path('', views.projecthomepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
