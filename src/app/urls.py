from django.urls import path,include
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('',TemplateView.as_view(template_name="base.html")),
    path('home/<str:url>',home_view),
    path('home/form/',FormView.as_view()),
    path('home/form/submit/<str:user>',FormView.as_view()),
    path('clients_added/<int:user_id>',clients_added),
    path('all_payments/',all_payments),
    path('paid_payments/',paid_payments),
    path('open_payments/',open_payments),
]