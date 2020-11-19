from django.db import models


class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField()


class Choice(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
