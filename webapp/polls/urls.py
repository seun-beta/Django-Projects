from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name ='polls'
urlpatterns = [
    path('', views.Index.as_view(), name='index' ),
    path('form', views.ClassView.as_view(), name='form'),
    path('dump', views.DumpPython.as_view(), name='dump'),
    path('reverse', views.ReversePython.as_view(), name='reverse'),

]
