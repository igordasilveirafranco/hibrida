from django.shortcuts import render
from ..advogado.models import Processo
# Create your views here.
def magistrado_one(request):
    processos = Processo.objects.all()
    return render(request,'magistrado_one.html',{"processos":processos})

def magistrado_detail(request,numero):
    processo = Processo.objects.get(numero=numero)

    return render(request,'magistrado_detail.html',{"processo":processo})