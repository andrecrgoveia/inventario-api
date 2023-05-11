# DETIC-PCCE1 - Desenvolvimento: Teste Pratico Back-end
Desenvolvedor: André Castelo

### Descrição
Criei um projeto chamado inventario-api, nesse projeto:
- É um sistema de inventário simples
- Relaciona objetos e pessoas que estejam de posse deles
- Diferencia os tipos de pessoas
- Diferencia os tipos de objetos
- Todos os endpoints possuem as operações básicas de um CRUD
- Todos os endpoints possuem filtros com base em cada campo do seu model

### Atividades Propostas
- Todas as atividades minimas foram atendidas
1: Foi implementada a modelagem partindo do esqueleto fornecido
2: Todos os endpoints possuem as operações básicas de CRUD
3: O endpoint de consulta que permitam filtrar os Objetos por Pessoa que os possui (Exemplo, http://0.0.0.0:8000/api/v1/possepessoaobjetos/?id_objeto=3)
4: O endpoint de consulta de PossePessoaObjeto deve trazer cada objeto com campos adicionais,
nos quais a Pessoa e o Objeto relacionados estejam representados com seus proprios campos. (Para visualizar essa condição, basta acessar o endpoint, http://0.0.0.0:8000/api/v1/possepessoaobjetos/)

### Condições adicionais
- Metade das condições adicionais foram atendidas
1: Condição atendida
2: Condição atendida

### Tecnologias utilizadas
- Python
- Django
- SQLite
- Docker

### Base de dados populada para demonstração
superuser
- email: super@user.com
- username: superuser
- password: superuser2023

### Como acesso o projeto?
Você pode rodar esse comando e o container será iniciado automaticamente:
- docker run --publish <ESCOLHA_A_PORTA>:8000 andrecrgoveia/inventario-api
- No browser vá até o endereço http://0.0.0.0:<ESCOLHA_A_PORTA>/

Rode esses dois comandos na raiz do projeto:
- docker-compose build
- docker-compose up
