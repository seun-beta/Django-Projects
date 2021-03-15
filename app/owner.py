from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        data = form.save(commit=False)
        data.owner = self.request.user
        data.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
