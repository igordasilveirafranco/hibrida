from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import shutil
import os
from .forms import DocumentForm
from random import randrange
from .models import Processo
from .motor import read_pdf_to_txt
# Create your views here.
def main_page(request):
    return render(request,'main/main_page.html')

def page_one(request):
    template = 'main/page_one.html'
    context = {}
    return render(request, template, context)

def page_two(request):
    template = 'main/page_two.html'
    print('aqui')
    if request.method == 'POST' and request.FILES['myfile']:
        proc =Processo.objects.create(
            arq=request.FILES['myfile'],
            numero=str(randrange(10000,99999))+str(randrange(10000,99999))+str(randrange(10000,99999))+str(randrange(10000,99999))
        )  
        form = DocumentForm()
        
        form.arq =request.FILES['myfile']        
        myfile = request.FILES['myfile']
        nome = myfile.name
        #read_pdf_to_txt(proc.arq.url,nome)
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
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'main/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request,'main/simple_upload.html')
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
   




