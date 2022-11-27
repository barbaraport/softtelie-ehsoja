
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
The ehSoja is a new module for recognizing soybean plants through the <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a> app! eSoja is a mobile application for the agricultor, in specific, soy farmers. eSoja provides its users with features that help them in monitoring, controlling and obtaining forecasts about their planting and harvesting. Our eSoja extension, ehSoja, enhances the native functions of the application and provides it with an innovation. Currently, the user needs to manually enter the number of pods within a plant so that the application can estimate the harvest data for them. Therefore, we developed the upload of a soybean plant image so that information like the amount of pods and grains per pod can be deduced through an analysis of the image. This functionality guarantees agility and versatility to the user, who will no longer need to make effort to obtain an estimate of his harvest.
</p>

<p align="center">🌱 See the eSoja app with our modifications <a href="https://github.com/barbaraport/esoja-mobile">here</a>! 🌿</p>
<p align="center">🌿 See the eSoja server with our modifications <a href="https://github.com/barbaraport/esoja-api">here</a>! 🌱</p>
<p align="center">🌱 See our dataset <a href="https://github.com/barbaraport/pods_dataset">here</a>! 🌿</p><br>

<h2 align="center">:bookmark_tabs: Sprint backlog :pencil:</h2>
<table height="230px">
    <tr>
        <td width="1000px"><p align="center">Estimate the size of the identified pods</p></td></tr>
    <tr>
        <td><p align="center">Estimate the amount of grains in each pod</p></td>
    <tr>
        <td><p align="center">Calculate the estimated amount of grains for each soy plant</p></td>
    <tr>
        <td><p align="center">Use the estimated amount of grains to fill the application with the obtained data</p></td>
    <tr>
</table>

<h2 align="center">:astronaut: User Stories :label:</h2>
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">I, as an user, can register samples of plants so that the system can count the amount of grains contained in each sample</p></td>
        <td><p align="justify">With the grains being counted by the system, I won't need to count it manually myself</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can see the estimated amount of grains per plant at the samples statistics page</p></td>
        <td><p align="justify">Knowing the amount of grains identified, I can decide whether to use this data or not</p></td>
    </tr>
    <tr>
        <td><p align="justify"> I, as an user, am able to use the other features that use the amount of grain's data</p></td>
        <td><p align="justify">By automatically having the estimated amount of grains and having this data correctly associated within the application, I can use other dependent features without wasting time counting it manually</p></td>
    </tr>
</table>

<h3>:question: What we did?</h3>
<p align="justify">In the 4th and last sprint, we updated the database model to store the estimated grains found in the soy plant, changed the interface of statistics to show the quantity of pods, grains and the productivity estimative and another places of the application that depends on this information.
</p>

<h3>:grey_question: Why?</h3>
<p align="justify">Since the main purpose of the recognition model was to estimate the amount of grains in each plant sample, implementing this functionality ensures that all the backlog requested by the client are being attended.
</p>
  
<h2>:running_woman: ehSoja running :computer::computer_mouse:</h2>
<p align="justify">In the GIF bellow, it is show the register of a new sample for the plot. The process is the same of the one in the previous sprint. Here, the difference is that in the statistics page of the sample, now is shown to the user the amount of estimated grains founds in each sample.
</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_4/ehSoja-Sprint-4.gif" height="600px"/>
</p>
  
<h3><i>:crossed_flags: Definition Of Ready</i></h3>
<p align="justify">The following artifacts were generated so that the team could start the development stage:</p>

- Sprint's epics
<table height="230px">
    <tr>
        <td width="1000px"><p align="center">Estimate the size of the identified pods</p></td></tr>
    <tr>
        <td><p align="center">Estimate the amount of grains in each pod</p></td>
    <tr>
        <td><p align="center">Calculate the estimated amount of grains for each soy plant</p></td>
    <tr>
        <td><p align="center">Use the estimated amount of grains to fill the application with the obtained data</p></td>
    <tr>
</table>

- User stories
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">I, as an user, can register samples of plants so that the system can count the amount of grains contained in each sample</p></td>
        <td><p align="justify">With the grains being counted by the system, I won't need to count it manually myself</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can see the estimated amount of grains per plant at the samples statistics page</p></td>
        <td><p align="justify">Knowing the amount of grains identified, I can decide whether to use this data or not</p></td>
    </tr>
    <tr>
        <td><p align="justify"> I, as an user, am able to use the other features that use the amount of grain's data</p></td>
        <td><p align="justify">By automatically having the estimated amount of grains and having this data correctly associated within the application, I can use other dependent features without wasting time counting it manually</p></td>
    </tr>
</table>

<h3><i>:crossed_flags: Definition Of Done :white_check_mark:</i></h3>
<p align="justify">Following the backlog gathered for the delivery of the sprint's valuable product, the artifacts generated for the costumer were:</p>

- [Source code](https://github.com/barbaraport/softtelie-ehsoja/tree/main/src)

- New functionality in the application: The user can now view in the plot's statistics page estimated amount of grains found by the detection model.
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_4/ehSoja-Sprint-4.gif" height="600px"/>
</p>

- The database model was updated to reflect the new data that is generated when registering a sample.

- The application now estimates the amount of grains for each plant in the moment of the register of a new sample for the plot.

<h2 align="center"><i>Burndown</i> :date::chart_with_downwards_trend:</h3>
<p align="justify">Looking at the burndown of the sprint, it's possible to see that the team was ahead of the time almost in all the sprint development, but in the end some delay occurred in the development of the product due to issues with development team members, but all under control.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Burndown/sprint_4.png"/>
</p>
  
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
