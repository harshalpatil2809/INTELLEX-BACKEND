from django.urls import path
from .views import register, login,logout,google_login_callback

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('google/callback/', google_login_callback, name='google_callback'),
]
