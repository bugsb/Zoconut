from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_user),
    path('logout_user/', views.logout_user),
]