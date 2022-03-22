# This file is created by Salman Abbasi
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # getting text
    djtext = request.POST.get('text','default')

    # checking check box values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('extraspaceremover','off')
    extraspaceremover= request.POST.get('fullcaps','off')
    numbercouter = request.POST.get('numbercouter', 'off')


    # check with check box is on
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                 analyzed = analyzed + char
        params = {'purpose':'removed punctuations', 'Analyzed_text': analyzed}
        djtext = analyzed
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase', 'Analyzed_text': analyzed}
        djtext = analyzed
    if (extraspaceremover =="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'Analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char

            else:
                print('no')
        params = {'purpose': 'Removed new lines', 'Analyzed_text': analyzed}
        djtext = analyzed

    if(numbercouter == "on"):
        analyzed = ""
        for char in djtext:
                analyzed = 'the total charachters are ', len(djtext)
        params = {'purpose': 'numbercouter', 'Analyzed_text': analyzed}
        djtext = analyzed
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numbercounter != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)