from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    # print(dir(request))
    # print(f"User: {request.user}")
    #if str(request.user) == 'AnonymousUser':
    #    teste = 'Usuário não logado'
    #else:
    #    teste = 'Usuário logado'
    context = {
        'curso': 'Programação Web com o Django Framework',
        'outro': 'Rafael é o CARA!',
        'produtos': produtos,
        # 'logado': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk) # configurar uma página não encontrada
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
