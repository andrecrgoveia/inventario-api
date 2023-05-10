# Importações
from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views


# Instanciando o roteador
router = routers.DefaultRouter()


# Registrando rotas das viewsets
router.register('tipopessoas', views.TipoPessoaViewSet)
router.register('pessoas', views.PessoaViewSet)
router.register('tipoobjetos', views.TipoObjetoViewSet)
router.register('objetos', views.ObjetoViewSet)
router.register('possepessoaobjetos', views.PossePessoaObjetoViewSet)


# Conectando a API usando roteamento automático de URL.
urlpatterns = [
    path('', include(router.urls)),
]
