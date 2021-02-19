from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import render

class ClassView(View):
    def get(self, request):
        return render(request, 'polls/form.html')
    
    def post(self, request):
        response = request.POST.get('input')
        context = {'input' : response}
        return render(request, 'polls/form.html', context)