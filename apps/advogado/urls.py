from django.urls import path
from .views import *
urlpatterns = [
    path('Informacoes/',page_one, name="page_one"),
    path('Assuntos/',page_two, name="page_two"),
    path('Autores/',page_three, name="page_three"),
    path('Reus/',page_four, name="page_four"),
    path('Documentos',page_five, name="page_five"),
    path('concluido',final_page, name="final_page"),
    path('sucesso',page_sucesso, name="page_sucesso"),
]