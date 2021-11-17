from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import Http404

from .models import Kit_Board
# Create your views here.


def index(request):
    Kit_Board_list = Kit_Board.objects.order_by('-KitBoard_ID')[:5]
    context = {
        'Kit_Board_list': Kit_Board_list
    }
    return render(request, 'KBMS/index.html', context)


def detail(request, KitBoard_ID):
    try:
        kitboard = Kit_Board.objects.get(KitBoard_ID=KitBoard_ID)
    except Kit_Board.DoesNotExist:
        raise Http404("开发板不存在")
    return render(request, 'KBMS/detail.html', {'kitboard': kitboard})
