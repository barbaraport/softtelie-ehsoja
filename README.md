<h1 align="center">:iphone: ehSoja 🌱</h1>

<p align="center">
    <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
    <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white"/>
    <img src="https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
    <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white"/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
    <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white"/>
    <img src="https://img.shields.io/badge/nestjs-%23E0234E.svg?style=for-the-badge&logo=nestjs&logoColor=white"/>
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
    <img src="https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white"/>
</p>

<p align="justify">
    O ehSoja é um novo módulo de para reconhecimento de plantas de soja dentro do <i>app</i> <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a>! O eSoja é uma aplicação <i>mobile</i> voltada ao público agricultor, em específico, agricultores de soja. O eSoja disponibiliza aos seus usuários funcionalidades que os ajudam a monitorar, controlar e obter previsões sobre seu plantio e colheita. Nossa extensão do eSoja, o ehSoja, incrementa as funções nativas da aplicação e provê uma inovação a ela. Atualmente o usuário necessita digitar manualmente a quantidade de vagens em uma planta para que ele possa estimar os dados da sua colheita. Sendo assim, desenvolvermos o <i>upload</i> de uma imagem da planta de soja e informações como quantia de vagens e grãos por vagem serão deduzidas através da análise desta imagem, garantindo mais rapidez e versatilidade ao usuário, que não precisará mais realizar esforço para obter a estimativa de colheita.
</p>

<h2><i>Product Backlog</i>:pushpin:</h2>
<p>Temos quatro <i>sprints</i> para o desenvolvimento da solução para o problema do nosso cliente. Sendo assim, priorizamos as funcionalidades desejadas de acordo com a imagem abaixo, de forma que cada entrega evolua em relação à última.</p>
<p align="center">
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/Backlog_Sprint1.png" width="400px">
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/Backlog_Sprint2.png" width="400px">
</p>
<p align="center">
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/Backlog_Sprint3.png" width="400px">
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/Backlog_Sprint4.png" width="400px">
</p>

<h2>:calendar: Cronograma das Entregas :spiral_calendar:</h2>
<table>
    <thead>
        <th width=100px>Entrega</th>
        <th width=450px>Descrição</th>
        <th width=70px>Disponibilidade</th>
        <th width=45px>Read-me</th>
        <th width=65px>Código-fonte</th>
    </thead>
    <tr>
        <td><p align="center">Entrega 1</p></td>
        <td><p align="justify">Treinamento de um modelo base para reconhecer e marcar os elementos da soja nas imagens de exemplo.</p></td>
        <td><p align="center">18/09</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Readmes/sprint_1.md">Visualizar</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.1">Baixar</a></p></td>
    </tr>
    <tr>
        <td><p align="center">Entrega 2</p></td>
        <td><p align="justify">O usuário poderá submeter imagens de seu plantio, que serão analisadas pelo algoritmo e poderá visualizar os resultados.</p></td>
        <td><p align="center">09/10</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/tree/main/docs/Readmes/sprint_2.md">Visualizar</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.2">Baixar</a></p></td>
    </tr>
    <tr>
        <td><p align="center">Entrega 3</p></td>
        <td><p align="justify">Contagem de vagens e atualização desses dados no banco de dados.</p></td>
        <td><p align="center">06/11</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/tree/main/docs/Readmes/sprint_3.md">Visualizar</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.3">Baixar</a></p></td>
    </tr>
    <tr>
        <td><p align="center">Entrega 4</p></td>
        <td><p align="justify">Realizar a estimativa de quantos grãos de soja estão presentes na planta.</p></td>
        <td><p align="center">27/11</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/tree/main/docs/Readmes/sprint_4.md">Visualizar</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.4">Baixar</a></p></td>
    </tr>
</table>

<h2>:running_woman: ehSoja em funcionamento :computer::computer_mouse:</h2>
<p align="justify">Abaixo estão as imagens que obtivemos a partir do treinamento do nosso modelo para a detecção das plantas e das suas vagens. Em alguns casos, as sombras foram reconhecidas como vagens, alguns pedaços das raízes das plantas e, também, algumas folhas. Devido a isso, precisamos implementar as devidas melhorias para esses problemas.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/10test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/11test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/14val_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/15test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/15val_result_cropped.png"/>
</p>

<h2>:girl: Integrantes da equipe :boy:</h2>
<ul>
    <li><a href="https://www.linkedin.com/in/b%C3%A1rbara-port-402158198/">Bárbara dos Santos Port</a> (<i>Scrum Master</i>)</li>
    <li><a href="https://www.linkedin.com/in/rafael-furtado-613a9712a/">Rafael Furtado Rodrigues dos Santos </a>(<i>Product Owner</i>)</li>
        <li><a href="https://www.linkedin.com/in/anna-carolina-de-oliveira-vale-mendes-372411b3">Anna Carolina de Oliveira Vale Mendes </a>(<i>Development Team</i>)</li>
    <li><a href="https://www.linkedin.com/in/anna-yukimi-yamada-6ba23b149/">Anna Yukimi Yamada </a>(<i>Development Team</i>)</li>
    <li><a href="https://www.linkedin.com/in/gabrielsouzati/">Gabriel Azevedo de Souza </a>(<i>Development Team</i>)</li>
    <li><a href="https://www.linkedin.com/in/mariaeduarda-oliveira/">Maria Eduarda Basílio de Oliveira </a>(<i>Development Team</i>)</li>
    <li><a href="https://www.linkedin.com/in/pedro-silva-18720b236/">Pedro Reginaldo Tomé Silva </a>(<i>Development Team</i>)</li>
</ul>
        
<p align="center">
    <img src="http://ForTheBadge.com/images/badges/built-with-love.svg"/>
</p>
