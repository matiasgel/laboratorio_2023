from django.urls import path
from libreria.views import *

urlpatterns=[path('autores/',AutoresList.as_view(),name='autores-list'),
             path('autor-create',AutorCreate.as_view(),name='autor-create')]