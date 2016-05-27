from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def news_list(request):
    template = "news/news_list.html"
    return render_to_response(template)