from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader

from paper_management.models import Paper


def index(request):
    paper_list = Paper.objects.all()
    context = {'paper_list': paper_list}
    return render(request, 'paper_management/index.html', context)


def paper_detail(request, paper_id):
    return HttpResponse(f"You'r looking at paper {paper_id}")
