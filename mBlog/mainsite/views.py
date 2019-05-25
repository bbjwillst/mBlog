from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Post


# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)