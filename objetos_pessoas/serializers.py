# Importações
from rest_framework import serializers
from .models import *


# Serializando o modelo TipoPessoa
class TipoPessoaSerializer(serializers.ModelSerializer):

    class Meta:        
        model = TipoPessoa       
        fields = '__all__'


# Serializando o modelo Pessoa
class PessoaSerializer(serializers.ModelSerializer):
    tipo_pessoa_descricao = serializers.CharField(source='tipo_pessoa.tipo',read_only=True)

    class Meta:        
        model = Pessoa       
        fields = '__all__'


# Serializando o modelo TipoObjeto
class TipoObjetoSerializer(serializers.ModelSerializer):

    class Meta:        
        model = TipoObjeto       
        fields = '__all__'


# Serializando o modelo Objeto
class ObjetoSerializer(serializers.ModelSerializer):
    tipo_objeto_descricao = serializers.CharField(source='tipo_objeto.tipo',read_only=True)

    class Meta:        
        model = Objeto       
        fields = '__all__'


# Serializando o modelo PossePessoaObjeto
class PossePessoaObjetoSerializer(serializers.ModelSerializer):
    numero_de_id_pessoa = serializers.CharField(source='id_pessoa.numero_de_id',read_only=True)
    tipo_pessoa = serializers.CharField(source='id_pessoa.tipo_pessoa',read_only=True)
    nome_pessoa = serializers.CharField(source='id_pessoa.nome',read_only=True)
    cpf_pessoa = serializers.CharField(source='id_pessoa.cpf',read_only=True)
    email_pessoa = serializers.CharField(source='id_pessoa.email',read_only=True)
    telefone_pessoa = serializers.CharField(source='id_pessoa.telefone',read_only=True)

    numero_de_id_objeto = serializers.CharField(source='id_objeto.numero_de_id',read_only=True)
    tipo_objeto = serializers.CharField(source='id_objeto.tipo_objeto',read_only=True)
    descricao_objeto = serializers.CharField(source='id_objeto.descricao',read_only=True)
    valor_estimado_objeto = serializers.CharField(source='id_objeto.valor_estimado',read_only=True)
    peso_objeto = serializers.CharField(source='id_objeto.peso',read_only=True)

    class Meta:        
        model = PossePessoaObjeto       
        fields = '__all__'
