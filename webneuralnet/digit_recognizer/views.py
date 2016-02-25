from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if (request.method == 'POST'):
        print(request.FILES['pic'])
        return HttpResponseRedirect('/')
    else:
        return render(request, 'digit_recognizer/index.html', {})