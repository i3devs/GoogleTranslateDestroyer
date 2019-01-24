from django.shortcuts import render

from .GTranslateDestroyer import GTranslateDestroyer
from .models import Destroyer


def index(request):
    context = {'input': "", 'output': "", 'langs': Destroyer.LANGS, 'default': "en"}
    return render(request, 'destroyer/index.html', context)


def destroy(request):
    if request.method == 'POST':
        text = request.POST.get('input', None)
        if len(text) > 0:
            destroyer = GTranslateDestroyer(text)
            output = destroyer.destroy()
            context = {'input': text, 'output': output, 'langs': Destroyer.LANGS, 'default': "en"}
            return render(request, 'destroyer/index.html', context)
        else:
            return render(request, 'destroyer/index.html')
    else:
        context = {'input': "", 'output': "", 'langs': Destroyer.LANGS, 'default': "en"}
        return render(request, 'destroyer/index.html', context)
