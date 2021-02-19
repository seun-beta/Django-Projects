from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='polls/index.html'), name='index' ),
    path('form', views.ClassView.as_view(), name='form'),

]