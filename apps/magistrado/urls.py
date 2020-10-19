from django.urls import path
from .views import *

urlpatterns = [
   path('magistrado',magistrado_one,name='magistrado_one'),
   path('magistrado_proc/<str:numero>',magistrado_detail,name='magistrado_detail')
]