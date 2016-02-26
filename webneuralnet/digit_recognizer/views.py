from django.shortcuts import render
from django.http import HttpResponseRedirect
from webneuralnet import settings
from PIL import Image
import re

# Create your views here.
def index(request):
    if (request.method == 'POST'):
        imgRaw = request.POST.get('pic')
        imgstr = re.search(r'base64,(.*)', imgRaw).group(1)
        output = open(settings.MEDIA_ROOT+'/output.png', 'wb')
        output.write(imgstr.decode('base64'))
        output.close()
        
        png = Image.open(settings.MEDIA_ROOT+'/output.png')
        png.load()
        
        background = Image.new("RGB", png.size, (255, 255, 255))
        background.paste(png, mask=png.split()[3])

        background.save('foo.jpg', 'JPEG', quality=80)
        return HttpResponseRedirect('/'); 
    else:
        return render(request, 'digit_recognizer/index.html', {})  