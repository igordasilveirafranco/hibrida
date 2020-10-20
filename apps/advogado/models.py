from django.db import models

class Processo(models.Model):
    
    cod_processo = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20)
    arq = models.FileField(upload_to="pdf/")
    tema = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering = ('numero',)

    def  __str__(self):
        return "numero: "+str(self.numero)+ "Tema: "+str(self.tema)


