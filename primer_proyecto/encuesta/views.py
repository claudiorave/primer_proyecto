from django.views.generic import ListView

from encuesta.models import Pregunta


class PreguntasView(ListView):
    model = Pregunta
