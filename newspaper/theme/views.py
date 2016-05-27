from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response


def base(request):
    template = "theme/base.html"
    return render_to_response(template)