from django.urls import path
from . import views

urlpatterns = [
    path('chatbot_view', views.chatbot_view, name='chatbot'),
    path('chatbot_index', views.chatbot_index, name='chatbot_index'),
]
