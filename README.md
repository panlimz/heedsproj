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

---
### Uma versão funcional desta aplicação está disponível através do Heroku, [aqui](https://heedswhereapp.herokuapp.com). 
---

## Como usar localmente
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

Esses passos devem ser suficientes pra que ele se torne funcional. Aqui estão algumas telas de exemplo:

## Aplicação em funcionamento
### __- HomePage__
![This is an image](https://lh3.googleusercontent.com/pw/AM-JKLWYWvEsToKF2dkhlZr5yWX8fPxp2G3yIdg9fTt-NDSaQGpYN__XrI5QSzXjFrW60zXpWV4k_euN2UVYdlrddjKTRZzXzHKtqGW1gs_0Ra10HA5Da60CVi8q8Hu2o9Vfd7jOLAseJ6mTetEoDCrqmxeA=w1792-h894-no?authuser=0)

### __- Adicionar um local__
![This is an image](https://lh3.googleusercontent.com/pw/AM-JKLV0rCEyxNgQ9fspXWKWda7KQGd6zGlFrFFnwH8uMFvPBo9qDDZXxmlza2yclqQY96WvgdN9UIgIVrQ1tfsHlOZtk3PuuzeHw2ESSbycP0KrGyZy3AsTVlSCDW-jYOIw_Aig8pFKcqcambms67569lMA=w1803-h894-no?authuser=0)

### __- Lista de locais__
![This is an image](https://lh3.googleusercontent.com/pw/AM-JKLUjldH03WGx0pmfuGk_VmMDeK61DGFFVqKJH8dpo6D_phA43o1PrpXiIfNYnXIrpvOK105T-T_4hJgOU688xEMwMqmAUQHHSSY7D0j-1hhYdmtv1RXfX5JJeo7nJraKXvUDHqsvKfO1x9ZZsCwQ79to=w1797-h894-no?authuser=0)

### __- Encontrar locais por região__
![This is an image](https://lh3.googleusercontent.com/pw/AM-JKLWc5V3xUsWdQE_jcFGY0pL85nG7PtCWlNibbHccuZGJ3bdnpy9KLLMA938AkKdVGwlZd5zT_0rlnR2CkMDK2RD9kwnsvaxROFzNzXLs_khvdIcjdKHDnnZuBi6E0lZRkbyNqDPbZxxwPrmU9TcbbK2v=w1807-h894-no?authuser=0)

### __- Encontrar locais por data__
![This is an image](https://lh3.googleusercontent.com/pw/AM-JKLVzoXl0QGyI7zBWuouVGO6BmGYGuH4-Gb-e2OTcQiprIkq_IAGvGSSb4NOr1KMyoM2KJHk5v-gq-TnKE5GbTRRzid-vg19SXKscAQSWA0honfz9HPolD6J9fpjju5qz10Cd4SUzGWLVOEhIjShnnw8q=w1790-h894-no?authuser=0)


Se você tem quaisquer feedbacks sobre este projeto, sinta-se à vontade em me contatar pelos meios disponíveis no meu [Perfil](https://github.com/panlimz). 