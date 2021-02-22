from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.shortcuts import redirect, render

class ClassView(View):
    def get(self, request):
        data = request.session.get('input', False)
        print(data)
        #if (data) : del(request.session['input'])
        return render(request, 'polls/form.html', {'input': data})
    
    def post(self, request):
        response = request.POST.get('input')
        request.session['input'] = response 
        print(request.session['input'])
        return redirect(request.path)