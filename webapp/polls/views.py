from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import resolve
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(View, LoginRequiredMixin):
    def get(self, request):
        return render(request, 'polls/index.html')


class ClassView(View):
    def get(self, request):
        #data = request.session.get('input', False)
        #print(data)
        #if (data) : del(request.session['input'])
        return render(request, 'polls/form.html')#, {'input': data})
    
    def post(self, request):
        response = request.POST.get('input')
        return HttpResponseRedirect('form')

class DumpPython(View):
    def get(self, request):
        resp = '<pre>\n User Data in Python:\n\n'
        resp += 'Login url:' + reverse('login') + '\n'
        resp += 'Logout url:' + reverse('logout') + '\n\n'

        return HttpResponse(resp)

class ReversePython(View):
    def get(self, request):
        resp = 'URL Reverse:\n\n' + reverse('password_change')

        return HttpResponse(resp)
