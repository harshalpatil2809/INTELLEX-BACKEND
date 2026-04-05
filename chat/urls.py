from django.urls import path
from .views import create_chat, send_message, get_chats, get_messages

urlpatterns = [
    path('create/', create_chat),
    path('send/', send_message),
    path('list/', get_chats),
    path('messages/<int:id>/', get_messages),
]