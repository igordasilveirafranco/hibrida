from django.forms import ModelForm
from .models import Processo


class DocumentForm(ModelForm):
    class Meta:
        model=Processo
        fields= ('numero','arq','tema')
