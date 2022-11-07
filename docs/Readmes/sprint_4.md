
<h1 align="center">:iphone: ehSoja 🌱</h1>

<p align="center">
    <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252"/>
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
    <img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white"/>
</p>

<p align="justify">
The ehSoja is a new module for recognizing soybean plants through the <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a> app! eSoja is a mobile application for the agricultors, in specific, soy farmers. eSoja provides its users with features that help them in monitoring, controlling and obtaining forecasts about their planting and harvesting. Our eSoja extension, ehSoja, enhances the native functions of the application and provides it with an innovation. Currently, the user needs to manually enter the number of pods within a plant so that the aplication can estimate the harvest data for them. Therefore, we developed the <i>upload</i> of a soybean plant image so that informations like the amount of pods and grains per pod can be deduced through an analysis of the image. This functionality guarantees agility and versatility to the user, who will no longer need to make effort to obtain an estimate of his harvest.
</p>

<p align="center">🌱 See the eSoja app with our modifications <a href="https://github.com/barbaraport/esoja-mobile">here</a>! 🌿</p>
<p align="center">🌿 See the eSoja server with our modifications <a href="https://github.com/barbaraport/esoja-api">here</a>! 🌱</p>
<p align="center">🌱 See our dataset <a href="https://github.com/barbaraport/pods_dataset">here</a>! 🌿</p><br>

<h2 align="center">:bookmark_tabs: Sprint backlog :pencil:</h2>
<table height="230px">
    <tr>
        <td width="1000px"><p align="center">Descobrir tamanho das vagens identificadas</p></td>
    </tr>
    <tr>
        <td><p align="center">Estimar quantia de grãos para cada vagem</p></td>
    <tr>
        <td><p align="center">Calcular quantia estimada de grãos para a planta de soja</p></td>
    <tr>
        <td><p align="center">Utilizar a quantia estimada de grãos da planta para alimentar a aplicação com esses dados</p></td>
    <tr>
</table>

<h2 align="center">:astronaut: User Stories :label:</h2>
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">Eu, como usuário, registro amostras de plantas para que o sistema conte quantos grãos estão em cada planta</p></td>
        <td><p align="justify">Com o sistema contando a quantia de grãos por mim, não preciso gastar tempo contando manualmente</p></td>
    </tr>
    <tr>
        <td><p align="justify">Eu, como usuário, consigo ver, na página de estatísticas das amostras, quantos grãos foram estimados para cada planta</p></td>
        <td><p align="justify">Ao ficar ciente da quantia de grãos que foram identificados nas amostras, posso julgar por mim mesmo se devo ou não utilizar esses dados</p></td>
    </tr>
    <tr>
        <td><p align="justify">Eu, como usuário, utilizo normalmente as outras funcionalidades da aplicação que dependam da informação de grãos por planta</p></td>
        <td><p align="justify">Ao ter a quantia de grãos estimadas automáticamente e ter essa informação corretamente associada na aplicação me permite utilizar rapidamente outras funcionalidades dependentes disso sem que tenha que gastar tempo contando manualmente a quantia de grãos da planta</p></td>
    </tr>
</table>

  <h3>:question: What we did?</h3>
  <p align="justify">TO-DO
  </p>

  <h3>:grey_question: Why?</h3>
  <p align="justify">TO-DO</p>
  
<h2>:running_woman: ehSoja running :computer::computer_mouse:</h2>
<p align="justify">TO-DO</p>
  
<h3><i>:crossed_flags: Definition Of Ready</i></h3>
<p align="justify">The following artifacts were generated so that the team could start the development stage:</p>

- Sprint's epics
<table height="230px">
    <tr>
        <td width="1000px"><p align="center">Descobrir tamanho das vagens identificadas</p></td>
    </tr>
    <tr>
        <td><p align="center">Estimar quantia de grãos para cada vagem</p></td>
    <tr>
        <td><p align="center">Calcular quantia estimada de grãos para a planta de soja</p></td>
    <tr>
        <td><p align="center">Utilizar a quantia estimada de grãos da planta para alimentar a aplicação com esses dados</p></td>
    <tr>
</table>

- User stories
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">Eu, como usuário, registro amostras de plantas para que o sistema conte quantos grãos estão em cada planta</p></td>
        <td><p align="justify">Com o sistema contando a quantia de grãos por mim, não preciso gastar tempo contando manualmente</p></td>
    </tr>
    <tr>
        <td><p align="justify">Eu, como usuário, consigo ver, na página de estatísticas das amostras, quantos grãos foram estimados para cada planta</p></td>
        <td><p align="justify">Ao ficar ciente da quantia de grãos que foram identificados nas amostras, posso julgar por mim mesmo se devo ou não utilizar esses dados</p></td>
    </tr>
    <tr>
        <td><p align="justify">Eu, como usuário, utilizo normalmente as outras funcionalidades da aplicação que dependam da informação de grãos por planta</p></td>
        <td><p align="justify">Ao ter a quantia de grãos estimadas automáticamente e ter essa informação corretamente associada na aplicação me permite utilizar rapidamente outras funcionalidades dependentes disso sem que tenha que gastar tempo contando manualmente a quantia de grãos da planta</p></td>
    </tr>
</table>

<h3><i>:crossed_flags: Definition Of Done :white_check_mark:</i></h3>
<p align="justify">Following the backlog gathered for the delivery of the sprint's valuable product, the artifacts generated for the costumer were:</p>

- [Source code](https://github.com/barbaraport/softtelie-ehsoja/tree/main/src)

<h2 align="center"><i>Burndown</i> :date::chart_with_downwards_trend:</h3>
<p align="justify">TO-DO</p>
  
<h2>:girl: Our team members :boy:</h2>
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
