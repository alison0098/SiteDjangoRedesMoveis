from django.shortcuts import render

from .models import Dados



def index(request):

    lim_temperatura=30
    lim_umidade=60
    temperatura_ideal=25
    umidade_ideal=50

    query = Dados.objects.raw('SELECT *, AVG(temperatura) as media_t,AVG(umidade) \
    as media_u FROM polls_dados GROUP BY local ')

    context = {'query': query,'lim_temperatura':lim_temperatura , 'lim_umidade':lim_umidade,'temperatura_ideal':temperatura_ideal,'umidade_ideal':umidade_ideal}
    return render(request, 'polls/index.html', context)

def foto(request,nome_local):

    query = Dados.objects.raw('SELECT id,local,presenca FROM polls_dados WHERE local="'+nome_local+'" AND presenca="HIGH"')

    context = {'query':query,'nome_local':nome_local}

    return render(request, 'polls/foto.html', context)


