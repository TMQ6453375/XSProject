from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # 请求的路径和请求方法
    print(request.path, request.method)
    print(request.GET.get('page'), request.GET.get('tag'))

    return render(request, 'art/list.html',
                  context={'name': 'ganbo'})
