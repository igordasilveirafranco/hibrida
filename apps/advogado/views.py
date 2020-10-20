from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import shutil
import os
from .forms import DocumentForm
from random import randrange
from .models import Processo
from .motor import read_pdf_to_txt
import unidecode
from unicodedata import normalize
# Create your views here.
def corrigirAcentos(texto):
    texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    if 'ç' in texto:
        texto = texto.replace('ç','c')
    return texto

def main_page(request):
    return render(request,'main/main_page.html')

def page_one(request):
    template = 'main/page_one.html'
    context = {}
    return render(request, template, context)

def page_two(request):
    template = 'main/page_two.html'
    if request.method == 'POST' and request.FILES['myfile']:
        
        proc =Processo.objects.create(
            arq=request.FILES['myfile'],
            numero=str(randrange(10000,99999))+str(randrange(10000,99999))+str(randrange(10000,99999))+str(randrange(10000,99999)),
        )  
        form = DocumentForm()
        
        form.arq =request.FILES['myfile']        
        myfile = request.FILES['myfile']
        nome = corrigirAcentos(myfile.name)
        proc.tema = read_pdf_to_txt(proc.arq.url,nome)
        proc.save()
        form.save(commit=False)
        return render(request, 'main/final_page.html',{'arquivo':proc})
    context = {}
    return render(request, template, context)

def page_three(request):
    template = 'main/page_three.html'
    context = {}
    return render(request, template, context)

def page_four(request):
    template = 'main/page_four.html'
    context = {}
    return render(request, template, context)

def page_five(request):

    template = 'main/page_five.html'
   

    context = {}
    return render(request, template, context)


def final_page(request):
    template = 'main/final_page.html'
    context = {}
    return render(request, template, context)

def move_arquivo(nome):
    arquivo = os.listdir("media/")
    shutil.move("media/"+arquivo[0],"static/pdf/"+arquivo[0])
   
def page_sucesso(request):
   template = 'main/page_sucesso.html'
   context = {}
   return render(request, template, context)
   




