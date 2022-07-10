from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index1.html")


def analyze(request):
    dj = request.POST.get("text", "default")
    remover = request.POST.get("removerpunc", "off")
    Capitalize = request.POST.get("Capitalize", "off")
    lineremovers = request.POST.get("new line remover", "off")
    spaceremovers = request.POST.get("extra space remover", "off")
    if remover == "on":
        punctuations = '''%,$,;,:,#,|'''
        analyzed = ""
        for char in dj:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuation', 'analyzed_text': analyzed}
        dj = analyzed

    if Capitalize == "on":
        analyzed = ""
        for char in dj:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'capitalize each word', 'analyzed_text': analyzed}
        dj = analyzed

    if lineremovers == "on":
        analyzed = ""
        for char in dj:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'remover extra lines', 'analyzed_text': analyzed}
        dj = analyzed

    if spaceremovers == "on":
        analyzed = ""
        for index, char in enumerate(dj):
            if not (dj[index] == " " and dj[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'remove extra space', 'analyzed_text': analyzed}

        if remover != "on" and lineremovers != "on" and Capitalize != "on" and spaceremovers != "on":
            return HttpResponse("please select any operation and try again")

    return render(request, "analyse2.html", params)
