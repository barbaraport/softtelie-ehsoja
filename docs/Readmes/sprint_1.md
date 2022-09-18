
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
    O ehSoja é um novo módulo de para reconhecimento de plantas de soja dentro do <i>app</i> <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a>! O eSoja é uma aplicação <i>mobile</i> voltada ao público agricultor, em específico, agricultores de soja. O eSoja disponibiliza aos seus usuários funcionalidades que os ajudam a monitorar, controlar e obter previsões sobre seu plantio. Nossa extensão do eSoja, o ehSoja, incrementa as funcionalidades nativas da aplicação e uma inovação a ela. Atualmente o usuário necessita digitar manualmente a quantidade de vagens em uma planta para que ele possa estimar os dados da sua colheita. Sendo assim, desenvolvermos o upload de uma imagem da planta de soja e informações como quantia de vagens e grãos por vagem serão deduzidas através da análise desta imagem, garantindo mais rapidez e versatilidade ao usuário, que não precisará mais realizar esforço para obter a estimativa de colheita.
</p>
  
  <h2 align="center">:rainbow::spiral_calendar: Primeira Entrega :stars:</h2>
  <h3>:question: O que fizemos?</h3>
  <p align="justify">Na sprint 1 decidimos iniciar o projeto dando um primeiro passo na identificação de vagens e sojas a partir das imagens de exemplo.
  </p>
  <p align="center">
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/Backlog_Sprint1.png" width="400px"/>
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/UserStories_Sprint01.png" width="400px"/>
  </p>
  <h3>:grey_question: Por quê?</h3>
  <p align="justify">Reconhecer a planta e as suas vagens em uma é o passo que mais demanda um bom refinamento do modelo criado para o reconhecimento dessas características. Sendo assim, entregamos uma primeira versão de forma a mostrar o nosso potencial e receber <i>feedbacks</i> de forma mais rápida para termos mais chances de obter um modelo próximo à perfeição.</p>
  
<h2>:running_woman: ehSoja em funcionamento :computer::computer_mouse:</h2>
<p align="justify">Abaixo estão as imagens que obtivemos a partir do treinamento do nosso modelo para a detecção das plantas e das suas vagens. Em alguns casos, as sombras foram reconhecidas como vagens, alguns pedaços das raízes das plantas e, também, algumas folhas. Devido a isso, precisamos implementar as melhorias para esses problemas.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/10test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/sprint_1_adjusts/docs/MVPs/sprint_1/11test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/sprint_1_adjusts/docs/MVPs/sprint_1/14val_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/sprint_1_adjusts/docs/MVPs/sprint_1/15test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/sprint_1_adjusts/docs/MVPs/sprint_1/15val_result_cropped.png"/>
</p>
  
<h3><i>:crossed_flags: Definition Of Ready</i></h3>
<p align="justify">Para que o desenvolvimento de cada requisito seja iniciado, é necessário que ele seja compreendido detalhadamente e seja fragmentado em diversas tarefas para os desenvolvedores. Posto isso, cada uma das pequenas tarefas que são geradas recebem uma descrição do que deve ser feito e uma prioridade. Tarefas que são mais difíceis ou que podem impossibilitar a realização de outra tarefa, geralmente têm prioridade máxima. Por fim, os desenvolvedores podem, proativamente, iniciar uma <i>task</i>.</p>

<h3><i>:crossed_flags: Definition Of Done :white_check_mark:</i></h3>
<p align="justify">Para que cada uma das tarefas seja dada como prontas e finalizadas, é necessário que o código seja revisado a fim de evitar duplicação de código, propor possíveis melhorias e verificar se realmente ele faz o que foi combinado. Após essa primeira avaliação, o sistema será executado pelo revisor a fim de verificar falhas e <i>bugs</i> que podem ter surgido após a implementação realizada. O código entrará em produção somente se estiver totalmente completo, validado e funcional.</p>


<h2 align="center"><i>Burndown</i> :date::chart_with_downwards_trend:</h3>
<p align="justify">Durante a nossa <i>sprint</i> tivemos várias dificuldades técnicas pois inteligência artificial é um novo assunto para nós. Mesmo assim, nos esforçamos pois temos o compromisso de realizar a entrega ao nosso cliente.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Burndown/sprint_1.png"/>
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
