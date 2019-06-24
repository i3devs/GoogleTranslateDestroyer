from django.shortcuts import render

from .GTranslateDestroyer import GTranslateDestroyer
from .models import Destroyer


def index(request):
    context = {'input': "", 'output': "", 'langs': Destroyer.LANGS, 'language': "en", 'langs_num': 99}
    return render(request, 'destroyer/index.html', context)


def destroy(request):
    if request.method == 'POST':
        text = request.POST.get('input', None)
        langs_num = request.POST.get('languages_number', None)
        lang = request.POST.get('initial_language', None)
        if len(text) > 0:
            try:
                destroyer = GTranslateDestroyer(text, langs_num, lang)

                output = destroyer.destroy()
                context = {'input': text, 'output': output, 'langs': Destroyer.LANGS, 'language': lang,
                           'langs_num': langs_num}
                return render(request, 'destroyer/index.html', context)
            except TypeError:
                return "The value inserted for the languages number is invalid."
        else:
            return render(request, 'destroyer/index.html')
    else:
        context = {'input': "", 'output': "", 'langs': Destroyer.LANGS, 'default': "en"}
        return render(request, 'destroyer/index.html', context)
