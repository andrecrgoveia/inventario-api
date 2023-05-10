# Importações
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *


# View do objeto TipoPessoa
class TipoPessoaViewSet(viewsets.ModelViewSet):
    queryset = TipoPessoa.objects.all()
    serializer_class = TipoPessoaSerializer

    # Filtro para listar o objeto pelo tipo
    def list(self, request):
        try:
            queryset = TipoPessoa.objects.all()
            tipo = self.request.query_params.get('tipo')
            if tipo is not None:
                queryset = queryset.filter(tipo=tipo)
            serializer = TipoPessoaSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View do objeto Pessoa
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.select_related('tipo_pessoa',).all()
    serializer_class = PessoaSerializer

    # Filtro para listar o objeto pelos campos do mesmo
    def list(self, request):
        try:
            queryset = Pessoa.objects.select_related('tipo_pessoa',).all()
            keys = [
                'numero_de_id',
                'tipo_pessoa',
                'nome',
                'cpf',
                'email',
                'telefone',
            ]
            filters = {}
            for key in keys:
                filter = self.request.query_params.getlist(key)
                if filter:
                    filters['{}__in'.format(key)] = filter
            queryset = queryset.filter(**filters)
            serializer = PessoaSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View do objeto TipoObjeto
class TipoObjetoViewSet(viewsets.ModelViewSet):
    queryset = TipoObjeto.objects.all()
    serializer_class = TipoObjetoSerializer

    # Filtro para listar o objeto pelo tipo
    def list(self, request):
        try:
            queryset = TipoObjeto.objects.all()
            tipo = self.request.query_params.get('tipo')
            if tipo is not None:
                queryset = queryset.filter(tipo=tipo)
            serializer = TipoObjetoSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    

# View do objeto Objeto
class ObjetoViewSet(viewsets.ModelViewSet):
    queryset = Objeto.objects.select_related('tipo_objeto',).all()
    serializer_class = ObjetoSerializer

    # Filtro para listar o objeto pelos campos do mesmo
    def list(self, request):
        try:
            queryset = Objeto.objects.select_related('tipo_objeto',).all()
            keys = [
                'numero_de_id',
                'tipo_objeto',
                'descricao',
                'valor_estimado',
                'peso',
            ]
            filters = {}
            for key in keys:
                filter = self.request.query_params.getlist(key)
                if filter:
                    filters['{}__in'.format(key)] = filter
            queryset = queryset.filter(**filters)
            serializer = ObjetoSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# View do objeto PossePessoaObjeto
class PossePessoaObjetoViewSet(viewsets.ModelViewSet):
    queryset = PossePessoaObjeto.objects.select_related('id_pessoa', 'id_objeto',).all()
    serializer_class = PossePessoaObjetoSerializer

    # Filtro para listar o objeto pelos campos do mesmo
    def list(self, request):
        try:
            queryset = PossePessoaObjeto.objects.select_related('id_pessoa', 'id_objeto',).all()
            keys = [
                'numero_de_id',
                'id_pessoa',
                'id_objeto',
            ]
            filters = {}
            for key in keys:
                filter = self.request.query_params.getlist(key)
                if filter:
                    filters['{}__in'.format(key)] = filter
            queryset = queryset.filter(**filters)
            serializer = PossePessoaObjetoSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
