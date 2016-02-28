from django.shortcuts import render
from django.http import HttpResponseRedirect
from webneuralnet import settings
import numpy as np
import mnist_loader
import network
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
        
        picSize = 28, 28
        background.thumbnail(picSize)
        background.save('foo_small.jpg', 'JPEG', quality=100)
        
        imgGrey = Image.open('foo_small.jpg').convert('L')
        imgArray = np.asarray(imgGrey)
        convertedArray = []
        for row in imgArray:
            for col in row:
                convertedArray.append(np.float32(abs(col-255))/255)
    
        print convertedArray
        return HttpResponseRedirect('/')
    else:
        return render(request, 'digit_recognizer/index.html', {})  