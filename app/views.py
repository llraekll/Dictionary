from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = Pydictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonyms(search)
    antonyms = dictionary.antonyms(search)
    context= {
        'meaning' : meaning,
        'synonyms' : synonyms,
        'antonyms' : antonyms
    }
    return render(request, context, 'word.html')