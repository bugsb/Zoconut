from django.urls import path,include
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('',TemplateView.as_view(template_name="base.html")),
    path('home/<str:url>',home_view),
    path('login/',TemplateView.as_view(template_name="login.html")),
    path('form/',FormView.as_view()),
    path('submit/',FormView.as_view()),
    path('data/',home),
    path('all_payments/',all_payments),
    path('paid_payments/',paid_payments),
    path('open_payments/',open_payments),
]