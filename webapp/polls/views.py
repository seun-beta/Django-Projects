from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View

def index(request):
    return HttpResponse('''Hello, world. You're at the polls index.
    It is great to have you here. This is one of my Django apps''')

def funky(request):
    response= '''
    <h1> This is the funky webpage </h1>  
    '''
    return HttpResponse(response)

def danger(request):
    response='''
    <html><body>
    <h3>This is the danger page. Your guess is 
    ''' + escape(request.GET['guess'])+'''</h3>
    </body>
    </html>  
    '''
    return HttpResponse(response)

def steam(request, guess):
    response='''
    <html><body>
    <h3>This is the danger page. Your guess is 
    ''' + escape(guess)+'''</h3>
    </body>
    </html>  
    '''
    return HttpResponse(response)
    
class ClassView1(View):
    def get(self, reqest):
        response = '''
        <html><body>
        <h4>Welcome to the ClassView1 HTML Page</h4>
        </body>
        </html>
        '''
        return HttpResponse(response)


class ClassView2(View):
    def get(self, request):
        response = '''
        <html><body>
        <h4>Welcome to the ClassView2 HTML Page</h4>
        </body>
        </html>
        '''
        return HttpResponse(response)


class ClassView3(View):
    def get(self, request, try1):
        response='''
    <html><body>
    <h3>This is ClassView3 page. Your guess is 
    ''' + escape(try1)+'''</h3>
    </body>
    </html>  
    '''
        return HttpResponse(response)


class ClassView4(View):
    def get(self, request, try2):
        response='''
        <html><body>
        <h3>This is ClassView3 page. Your guess is 
        ''' + escape(try2)+'''</h3>
        </body>
        </html>  
        '''
        return HttpResponse(response)

class BounceView(View):
    def get(self, request):
        return HttpResponseRedirect('https://www.google.com')