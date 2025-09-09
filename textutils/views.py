from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    params = {}

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = "".join([char for char in djtext if char not in punctuations])
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = "".join([char for char in djtext if char not in ("\n", "\r")])
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (char == " " and index+1 < len(djtext) and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = len(djtext)
        params = {
            'purpose': 'Let\'s Count the Characters',
            'count': analyzed,
            'heading': 'Total Characters in the Text - ',
        }

    if not params:
        return render(request, 'index.html', {'error': 'Please select at least one option'})

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
