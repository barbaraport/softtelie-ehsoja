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
    <img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white"/>
</p>

<p align="justify">
The ehSoja is a new module for recognizing soybean plants through the <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a> app! eSoja is a mobile application for the agricultors, in specific, soy farmers. eSoja provides its users with features that help them in monitoring, controlling and obtaining forecasts about their planting and harvesting. Our eSoja extension, ehSoja, enhances the native functions of the application and provides it with an innovation. Currently, the user needs to manually enter the number of pods within a plant so that the aplication can estimate the harvest data for them. Therefore, we developed the <i>upload</i> of a soybean plant image so that informations like the amount of pods and grains per pod can be deduced through an analysis of the image. This functionality guarantees agility and versatility to the user, who will no longer need to make effort to obtain an estimate of his harvest.
</p>

<p align="center">🌱 See the eSoja app with our modifications <a href="https://github.com/barbaraport/esoja-mobile">here</a>! Or see the eSoja server with our modifications <a href="https://github.com/barbaraport/esoja-api">here</a>! 🌱</p>

<h2><i>Product Backlog</i>:pushpin:</h2>
<p>We have four sprints, each one lasting three weeks, dedicated to the development of our client's issue's solution. That being said, we prioritize the desired features according to the table below, so that each sprint will have improvements over the previous one.</p>

<h2 align="center">:test_tube: Sprint 1</h2>
<table>
    <tr>
        <td width="1000px"><p align="center">Basic model training to localize soy plants in an image :heavy_check_mark:</p></td>
    </tr>
    <tr>
        <td><p align="center">Basic model training to localize pods in soy plants within an image:heavy_check_mark:</p></td>
    </tr>
    <tr>
        <td><p align="center">Marking the pods found in the soy plant :heavy_check_mark:</p></td>
    </tr>
</table>
<h2 align="center">:test_tube: Sprint 2</h2>
<table>
    <tr>
        <td width="1000px"><p align="center">Create/change the old plant's registration interface to give to the user access to the new functionalities :heavy_check_mark:</p></td>
    </tr>
    <tr>
        <td><p align="center">Create an interface that allows the user to visualize the image analysis result :heavy_check_mark:</p></td>
    </tr>
</table>
<h2 align="center">:test_tube: Sprint 3</h2>
<table>
    <tr>
        <td width="1000px"><p align="center">Enhance the recognition model of pods :triangular_flag_on_post:</p></td>
    </tr>
    <tr>
        <td><p align="center">Count how many pods have been found in the soy plant :triangular_flag_on_post:</p></td>
    </tr>
</table>
<h2 align="center">:test_tube: Sprint 4</h2>
<table>
    <tr>
        <td width="1000px"><p align="center">Train the model so it can recognize the amount of seeds in each pod :triangular_flag_on_post:</p></td>
    </tr>
    <tr>
        <td><p align="center">Fill in the total numbers of pods on the soy plant according to the image analysis :triangular_flag_on_post:</p></td>
    </tr>
</table>

<h2>:calendar: Delivery Schedule :spiral_calendar:</h2>
<table>
    <thead>
        <th width=100px>Sprint</th>
        <th width=450px>Description</th>
        <th width=70px>Availability</th>
        <th width=45px>Read-me</th>
        <th width=65px>Source code</th>
    </thead>
    <tr>
        <td><p align="center">Sprint 1</p></td>
        <td><p align="justify">Training a base model to recognize and mark the soy elements on the example images</p></td>
        <td><p align="center">18/09</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Readmes/sprint_1.md">View</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.1">Download</a></p></td>
    </tr>
    <tr>
        <td><p align="center">Sprint 2</p></td>
        <td><p align="justify">The user can submit images of his planting to be analyzed by the algorithm which will return the results</p></td>
        <td><p align="center">09/10</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/tree/main/docs/Readmes/sprint_2.md">View</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.2">Download</a></p></td>
    </tr>
    <tr>
        <td><p align="center">Sprint 3</p></td>
        <td><p align="justify">Counting pods and updating its data in the database</p></td>
        <td><p align="center">06/11</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/tree/main/docs/Readmes/sprint_3.md">View</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.3">Download</a></p></td>
    </tr>
    <tr>
        <td><p align="center">Sprint 4</p></td>
        <td><p align="justify">Estimate how many soybeans there are in the soy plant</p></td>
        <td><p align="center">27/11</p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/tree/main/docs/Readmes/sprint_4.md">View</a></p></td>
        <td><p align="center"><a href="https://github.com/barbaraport/softtelie-ehsoja/releases/tag/v0.4">Download</a></p></td>
    </tr>
</table>

<h2>:running_woman: ehSoja in action :computer::computer_mouse:</h2>
<p align="justify">For this sprint we integrated the application with the dispatch of the images and the recognition of the pods in the images. You can click on the preview preview option to quickly analyze only the chosen image, or finish importing all the images so that in the last step the request is made automatically and all the images are analyzed at once.

Compared to the last sprint, we started training a model that does the segmentation of the pods, and not just their location in the image.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_2/ehSoja-Sprint-2.gif" height="600px"/>
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
