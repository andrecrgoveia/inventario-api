# Importações
from django.contrib import admin
from .models import *


# Registrando o modelo TipoPessoa
admin.site.register(TipoPessoa)

# Registrando o modelo Pessoa
admin.site.register(Pessoa)

# Registrando o modelo TipoObjeto
admin.site.register(TipoObjeto)

# Registrando o modelo Objeto
admin.site.register(Objeto)

# Registrando o modelo PossePessoaObjeto
admin.site.register(PossePessoaObjeto)
