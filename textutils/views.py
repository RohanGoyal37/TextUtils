from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', '')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    analyzed = djtext

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = "".join([char for char in analyzed if char not in punctuations])

    if fullcaps == 'on':
        analyzed = analyzed.upper()

    if newlineremover == 'on':
        analyzed = "".join([char for char in analyzed if char not in ("\n", "\r")])

    if extraspaceremover == 'on':
        analyzed = " ".join(analyzed.split())

    # ✅ Count characters & words properly
    character_count = len(analyzed) if charcount == 'on' else None
    word_count = len(analyzed.split()) if charcount == 'on' else None

    if (removepunc == fullcaps == newlineremover == extraspaceremover == charcount == 'off'):
        return render(request, 'index.html', {'error': 'Please select at least one option'})

    return render(request, 'analyze.html', {
        'analyzed_text': analyzed,
        'count': character_count,
        'word_count': word_count,
        'purpose': "Text Analyzed Successfully ✅",
        'heading': "Total Characters"
    })


    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')