from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.owner import OwnerCreateView, OwnerDeleteView, OwnerUpdateView
from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


from app.models import Advert


class AdvertListView(ListView):
    model = Advert


class FullAdvertListView(LoginRequiredMixin, ListView):
    model = Advert


class AdvertDetailView(LoginRequiredMixin, DetailView):
    model = Advert


class AdvertCreateView(OwnerCreateView):
    model = Advert
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('app:all_ad')


class AdvertUpdateView(OwnerUpdateView):
    model = Advert
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('app:all_ad')


class AdvertDeleteView(OwnerDeleteView):
    model = Advert
    success_url = reverse_lazy('app:all_ad')
