from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import *


# Testes para o modelo TipoPessoa
class TipoPessoaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='superuser',
            email='super@user.com',
            password='superuser2023'
        )
        self.client.force_authenticate(user=self.user)
        self.tipo_pessoa = TipoPessoa.objects.create(tipo='Pessoa Física')
    
    def test_listar_tipos_pessoa(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/tipopessoas/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tipo_pessoa.tipo)

    def test_criar_tipo_pessoa(self):
        data = {'tipo': 'Pessoa Jurídica'}
        response = self.client.post('http://127.0.0.1:8000/api/v1/tipopessoas/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TipoPessoa.objects.count(), 2)
        self.assertEqual(TipoPessoa.objects.last().tipo, 'Pessoa Jurídica')

    def test_filtrar_tipo_pessoas_por_tipo(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/tipopessoas/?tipo=Pessoa Física')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tipo_pessoa.tipo)

    def test_atualizar_tipo_pessoa(self):
        data = {'tipo': 'Pessoa Jurídica'}
        response = self.client.put(f'http://127.0.0.1:8000/api/v1/tipopessoas/{self.tipo_pessoa.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.tipo_pessoa.refresh_from_db()
        self.assertEqual(self.tipo_pessoa.tipo, 'Pessoa Jurídica')

    def test_remover_tipo_pessoa(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/v1/tipopessoas/{self.tipo_pessoa.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(TipoPessoa.objects.count(), 0)


# Testes para o modelo Pessoa
class PessoaAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='superuser',
            email='super@user.com',
            password='superuser2023'
        )
        self.client.force_authenticate(user=self.user)
        self.tipo_pessoa = TipoPessoa.objects.create(tipo='Pessoa Física')
        self.pessoa = Pessoa.objects.create(
            numero_de_id=1,
            tipo_pessoa=self.tipo_pessoa,
            nome='Fulano',
            cpf=12345678910,
            email='fulano@teste.com',
            telefone=123456789
        )

    def test_listar_pessoas(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/pessoas/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pessoa.nome)

    def test_criar_pessoa(self):
        data = {
            'numero_de_id': 2,
            'tipo_pessoa': self.tipo_pessoa.id,
            'nome': 'Beltrano',
            'cpf': 98765432101,
            'email': 'beltrano@teste.com',
            'telefone': 987654321
        }
        response = self.client.post('http://127.0.0.1:8000/api/v1/pessoas/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Pessoa.objects.count(), 2)
        self.assertEqual(Pessoa.objects.last().nome, 'Beltrano')

    def test_filtrar_pessoas_por_tipo_pessoa(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/pessoas/?tipo_pessoa=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pessoa.nome)

    def test_filtrar_pessoas_por_nome(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/pessoas/?nome=Fulano')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pessoa.nome)

    def test_filtrar_pessoas_por_cpf(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/pessoas/?cpf=12345678910')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pessoa.nome)

    def test_filtrar_pessoas_por_email(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/pessoas/?email=fulano@teste.com')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pessoa.nome)

    def test_filtrar_pessoas_por_telefone(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/pessoas/?telefone=123456789')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pessoa.nome)

    def test_atualizar_pessoa(self):
        data = {
            'numero_de_id': 1,
            'tipo_pessoa': self.tipo_pessoa.id,
            'nome': 'Fulano de Tal',
            'cpf': 12345678910,
            'email': 'fulano@teste.com',
            'telefone': 123456789
        }
        response = self.client.put(f'http://127.0.0.1:8000/api/v1/pessoas/{self.pessoa.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.pessoa.refresh_from_db()
        self.assertEqual(self.pessoa.nome, 'Fulano de Tal')

    def test_remover_pessoa(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/v1/pessoas/{self.pessoa.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Pessoa.objects.count(), 0)


# Testes para o modelo TipoObjeto
class TipoObjetoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='superuser',
            email='super@user.com',
            password='superuser2023'
        )
        self.client.force_authenticate(user=self.user)
        self.tipo_objeto = TipoObjeto.objects.create(
            tipo='Objeto Físico',
            multiplas_posses=True
        )
    
    def test_listar_tipos_objeto(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/tipoobjetos/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tipo_objeto.tipo)

    def test_criar_tipo_objeto(self):
        data = {'tipo': 'Objeto Digital', 'multiplas_posses': False}
        response = self.client.post('http://127.0.0.1:8000/api/v1/tipoobjetos/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TipoObjeto.objects.count(), 2)
        tipo_objeto_criado = TipoObjeto.objects.last()
        self.assertEqual(tipo_objeto_criado.tipo, 'Objeto Digital')
        self.assertFalse(tipo_objeto_criado.multiplas_posses)

    def test_filtrar_tipo_objeto_por_tipo(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/tipoobjetos/?tipo=Objeto Físico')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tipo_objeto.tipo)

    def test_atualizar_tipo_objeto(self):
        data = {'tipo': 'Objeto Digital', 'multiplas_posses': False}
        response = self.client.put(f'http://127.0.0.1:8000/api/v1/tipoobjetos/{self.tipo_objeto.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.tipo_objeto.refresh_from_db()
        self.assertEqual(self.tipo_objeto.tipo, 'Objeto Digital')
        self.assertFalse(self.tipo_objeto.multiplas_posses)

    def test_remover_tipo_objeto(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/v1/tipoobjetos/{self.tipo_objeto.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(TipoObjeto.objects.count(), 0)


# Testes para o modelo Objeto
class ObjetoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='superuser',
            email='super@user.com',
            password='superuser2023'
        )
        self.client.force_authenticate(user=self.user)
        self.tipo_objeto = TipoObjeto.objects.create(tipo='Livro', multiplas_posses=False)
        self.objeto = Objeto.objects.create(
            numero_de_id=1,
            tipo_objeto=self.tipo_objeto,
            descricao='Kindle',
            valor_estimado=500.00,
            peso=0.2
        )

    def test_listar_objetos(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/objetos/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.objeto.descricao)

    def test_criar_objeto(self):
        tipo_objeto = TipoObjeto.objects.create(tipo='Celular', multiplas_posses=True)
        data = {
            'numero_de_id': 2,
            'tipo_objeto': tipo_objeto.id,
            'descricao': 'iPhone',
            'valor_estimado': 5000.00,
            'peso': 0.5
        }
        response = self.client.post('http://127.0.0.1:8000/api/v1/objetos/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Objeto.objects.count(), 2)
        self.assertEqual(Objeto.objects.last().descricao, 'iPhone')

    def test_filtrar_objetos_por_numero_de_id(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/objetos/?numero_de_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.objeto.descricao)

    def test_filtrar_objetos_por_tipo_objeto(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/objetos/?tipo_objeto=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.objeto.descricao)

    def test_filtrar_objetos_por_descricao(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/objetos/?descricao=Kindle')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.objeto.descricao)

    def test_filtrar_objetos_por_valor_estimado(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/objetos/?valor_estimado=500.00')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.objeto.descricao)

    def test_filtrar_objetos_por_peso(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/objetos/?peso=0.2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.objeto.descricao)

    def test_atualizar_objeto(self):
        tipo_objeto = TipoObjeto.objects.create(tipo='Eletrônico', multiplas_posses=True)
        data = {
            'numero_de_id': 1,
            'tipo_objeto': tipo_objeto.id,
            'descricao': 'Kindle 2.0',
            'valor_estimado': 750.00,
            'peso': 0.2
        }
        response = self.client.put(f'http://127.0.0.1:8000/api/v1/objetos/{self.objeto.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.objeto.refresh_from_db()
        self.assertEqual(self.objeto.descricao, 'Kindle 2.0')
        self.assertEqual(self.objeto.valor_estimado, 750.00)

    def test_remover_objeto(self):
        response = self.client.delete(f'http://127.0.0.1:8000/api/v1/objetos/{self.objeto.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Objeto.objects.count(), 0)
