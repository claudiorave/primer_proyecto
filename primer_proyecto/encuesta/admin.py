from django.contrib import admin

# Register your models here.
from encuesta.models import (
    Pregunta,
    Choice
)

# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Choice)
