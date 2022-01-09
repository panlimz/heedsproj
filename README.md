## Bem vindo ao Where App!

A aplicação "Where", é uma aplicação desenvolvida utilizando o framework Django, a fim de armazenar informações dos locais já visitados em um banco de dados. Estes dados poderão ser inseridos, editados, filtrados e listados pelo usuário, que não requer cadastro para manipulação dos dados. 

Os pacotes necessários para essa aplicação estão listadas em 'requirements.txt'.

## Funções
### **Adicionar um local**
Esta aplicação possibita a adição de um novo local à partir da página inicial, ao acessar o menu suspenso _> Places > Add a Place._

### **Editar um local**
É possível editar um local ao selecioná-lo em sua lista de locais, disponível à partir da página inicial em ao acessar o menu suspenso _> Places > List Places._
<br>Ao acessar o local, também é possível deletá-lo.

### **Visualizar locais**
Além da lista mencionada acima, também é possível visualizar os locais através de dois filtros: por data e região.
<br>Em _> Places > Find Places._ as duas opções de busca são mostradas, e funcionam da seguinte maneira:
<br>**- Find Places by Region** exibe um formulário onde pode ser possível descrever qualquer local do globo. O mapa à sua esquerda retorna a exibição daquela localização, e é possível detectar qualquer local destacado por um marcador.
<br>**- Find Places by Date** exibe um formulário onde pode ser possível descrever qualquer data. À sua esquerda será exibida uma lista com o nome de todos os locais visitados naquela data.

> Tentei disponibilizar esta aplicação em pleno funcionamento através do Heroku, [aqui](https://heedswhereapp.herokuapp.com). Neste momento, ainda está em desenvolvimento (parcialmente funcional).

## Como usar
Este projeto ainda possui algumas limitações, portanto, é necessário configurar seu próprio banco de dados local (foi utilizado postgreSQL) em _settings.py._, conforme a seguir:
<br>
<pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nomedoservidor',
        'USER': 'usuariodoservidor',
        'PASSWORD': 'senhadoservidor',
        'HOST': 'localhost',
        'PORT': '5432',
    }</code></pre>

Para iniciar o servidor, basta abrir o terminal do projeto e executar:
<pre><code>python manage.py runserver</code></pre>

Também (ainda) é necessário que já existam dados de busca, portanto é necessário possuir um super usuário para acesso ao admin, através de:
<pre><code>python manage.py createsuperuser</code></pre>

Ao acessar a página de administrador, basta adicionar dados à _Searchdates_ e _Searchs_.

