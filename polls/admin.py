from django.contrib import admin

from .models import Dados
from .models import Imagem

admin.site.register(Dados)
admin.site.register(Imagem)
