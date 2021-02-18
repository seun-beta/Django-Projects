from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('main', TemplateView.as_view(template_name='polls/main.html')),
    path('default', TemplateView.as_view(template_name='polls/default.html')),
    path('', views.index, name='index'),
    path('funky', views.funky),
    path('danger', views.danger),
    path('steam/<int:guess>', views.steam),
    path('class1', views.ClassView1.as_view()),
    path('class2', views.ClassView2.as_view()),
    path('ClassView1/<int:try1>', views.ClassView3.as_view()),
    path('ClassView2/<slug:try2>', views.ClassView3.as_view()),
    path('bounce', views.BounceView.as_view()),
]