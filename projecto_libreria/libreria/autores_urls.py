from django.urls import path
from libreria.views import AutoresList

urlpatterns=[path('autores/',AutoresList.as_view())]