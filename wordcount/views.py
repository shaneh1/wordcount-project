from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def about(request):
    return render(request, 'about.html')

def analysis(request):
    return HttpResponse('<h1>This is the page which will contain analysis</h1>')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1


    sorted_words = sorted(word_dict.items(),
     key = operator.itemgetter(1),
     reverse = True)
    return render(request,
    'count.html',
    {'fulltext': fulltext,
    'count': len(wordlist), 'sorted_words': sorted_words})
