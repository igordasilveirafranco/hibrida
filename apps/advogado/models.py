from django.db import models

class Processo(models.Model):
    TEMA_CHOICES = (
        (0, "1007"),
        (1, "OUTROS"),
    )
    cod_processo = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20)
    arq = models.FileField(upload_to="pdf/")
    tema = models.CharField(max_length=1, choices=TEMA_CHOICES, blank=False, null=False,default=1)
    class Meta:
        ordering = ('numero',)

    def  __str__(self):
        return "numero: "+str(self.numero)+ "Tema: "+self.tema


