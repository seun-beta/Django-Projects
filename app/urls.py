from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.AdvertListView.as_view(), name='all'),
    path('ad', views.FullAdvertListView.as_view(), name='all_ad'),
    path('ad_detail/<int:pk>', views.AdvertDetailView.as_view(), name='ad_detail'),
    path('ad_create', views.AdvertCreateView.as_view(), name='ad_create'),
    path('ad_update/<int:pk>', views.AdvertUpdateView.as_view(), name='ad_update'),
    path('ad_delete/<int:pk>', views.AdvertDeleteView.as_view(), name='ad_delete'),

]
