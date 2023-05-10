# Importações
from django.db import models


'''
Essa classe fornece dois parâmetros, criado e alterado, para as outras classes herdarem
'''

# Classe base
class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    alterado = models.DateField('Alterado', auto_now=True)

    class Meta:
        abstract = True


# Nessa classe são criados os objetos que representam os tipos de pessoas
class TipoPessoa(Base):
    tipo = models.CharField('Tipo', max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'TipoPessoa'
        verbose_name_plural = 'TipoPessoas'

    def __str__(self):
        return str(self.tipo)
    

# Nessa classe são criados os objetos que representam as pessoas
class Pessoa(Base):
    numero_de_id = models.PositiveIntegerField('Numero de ID', blank=False, null=False)
    tipo_pessoa = models.ForeignKey(TipoPessoa, related_name='tipo_pessoa', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=255, blank=False, null=False)
    cpf = models.IntegerField('CPF', blank=False, null=False)
    email = models.EmailField('Email', max_length=255, blank=False, null=False)
    telefone = models.PositiveIntegerField('Telefone', blank=False, null=False)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return str(self.numero_de_id)
    

# Nessa classe são criados os objetos que representam os tipos de objetos
class TipoObjeto(Base):
    tipo = models.CharField('Tipo', max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'TipoObjeto'
        verbose_name_plural = 'TipoObjetos'

    def __str__(self):
        return str(self.tipo)
    

# Nessa classe são criados os objetos que representam os objeto
class Objeto(Base):
    numero_de_id = models.PositiveIntegerField('Numero de ID', blank=False, null=False)
    tipo_objeto = models.ForeignKey(TipoObjeto, related_name='tipo_objeto', on_delete=models.CASCADE)
    descricao = models.CharField('Descrição', max_length=255, blank=False, null=False)
    valor_estimado = models.FloatField('Valor Estimado', blank=False, null=False)
    peso = models.FloatField('Peso', blank=False, null=False)

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'

    def __str__(self):
        return str(self.numero_de_id)


# Nessa classe são criados os objetos que representam os tipos de posse de objetos por pessoas
class PossePessoaObjeto(Base):
    numero_de_id = models.PositiveIntegerField('Numero de ID', blank=False, null=False)
    id_pessoa = models.ForeignKey(Pessoa, related_name='id_pessoa', on_delete=models.CASCADE)
    id_objeto = models.ForeignKey(Objeto, related_name='id_objeto', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PossePessoaObjeto'
        verbose_name_plural = 'PossePessoaObjetos'

    def __str__(self):
        return str(self.numero_de_id)
