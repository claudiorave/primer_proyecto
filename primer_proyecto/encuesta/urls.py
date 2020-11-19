from django.urls import path
from encuesta.views import PreguntasView

urlpatterns = [
    path('preguntas/', PreguntasView.as_view()),
]
