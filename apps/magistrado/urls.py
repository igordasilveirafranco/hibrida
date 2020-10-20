from django.urls import path
from .views import *

urlpatterns = [
   path('magistrado',magistrado_one,name='magistrado_one'),
   path('magistrado_proc/<str:numero>',magistrado_detail,name='magistrado_detail'),
   path('MagistradoSucesso',magis_success, name="magis_success"),
   path('MagistradoNeg',mags_neg, name="mags_neg"),
]