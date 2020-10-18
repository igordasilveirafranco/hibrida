import os, sys
import textract 
from django.core.files.storage import FileSystemStorage
import time

def read_pdf_to_txt(path="",nome=""):
    #t1 = time.time()
    files =path
    cwd = os.getcwd()
    print(cwd+files)
    text = textract.process("{}".format(cwd+files), method='tesseract', encoding='utf-8')
    texto = text.decode('utf-8')

    #tempoExec = time.time() - t1
    #print("Tempo de execução: {} segundos".format(tempoExec/60))