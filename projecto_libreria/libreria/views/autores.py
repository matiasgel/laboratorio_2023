from typing import Any, Dict
from django.views.generic import *
from libreria.models import *
from django.core.paginator import Paginator


class AutoresList(TemplateView):
    template_name='listado_autores.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                    
        libros = Autor.objects.all()
        paginador = Paginator(libros, 12)
        numero_pagina = self.request.GET.get('page')
        context['page_obj'] = paginador.get_page(numero_pagina)
        return context