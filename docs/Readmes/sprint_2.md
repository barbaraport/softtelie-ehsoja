
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
The ehSoja is a new module for recognizing soybean plants through the <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a> app! eSoja is a mobile application for the agricultor, in specific, soy farmers. eSoja provides its users with features that help them in monitoring, controlling and obtaining forecasts about their planting and harvesting. Our eSoja extension, ehSoja, enhances the native functions of the application and provides it with an innovation. Currently, the user needs to manually enter the number of pods within a plant so that the application can estimate the harvest data for them. Therefore, we developed the <i>upload</i> of a soybean plant image so that information like the amount of pods and grains per pod can be deduced through an analysis of the image. This functionality guarantees agility and versatility to the user, who will no longer need to make effort to obtain an estimate of his harvest.
</p>

<p align="center">🌱 See the eSoja app with our modifications <a href="https://github.com/barbaraport/esoja-mobile">here</a>! Or see the eSoja server with our modifications <a href="https://github.com/barbaraport/esoja-api">here</a>! 🌱</p>

<h2 align="center">:bookmark_tabs: Sprint backlog :pencil:</h2>
<table>
    <tr>
        <td width="1000px"><p align="center">Create/change the old plant's registration interface to give to the user access to the new functionalities</p></td>
    </tr>
    <tr>
        <td><p align="center">Create an interface that allows the user to visualize the image analysis result</p></td>
    </tr>
</table>

<h2 align="center">:astronaut: User Stories :label:</h2>
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">I, as an user, have access to the new interface to register a plant</p></td>
        <td><p align="justify">With the access to the new interface, I can register a plant with the new requested data</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can take a new photo by the application to register a plant</p></td>
        <td><p align="justify">Taking a photo without have to photograph it previously make the steps be faster</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can choose a photo from my gallery to register a plant</p></td>
        <td><p align="justify">If I already has the photo of the plant that I want to register, choosing it from my gallery will speed up the steps</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, submit the plant’s photo to be analyzed</p></td>
        <td><p align="justify">Submitting the plant's photo be analyzed will allow me to know if I submit a good photo</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, receive the analyzed image with the identified elements marked on it
to check if the identification is satisfactory</p></td>
        <td><p align="justify">Receiving the analyzed photo will allow me to check if the submitted photo was good and ensure that I will only register if the analysis satisfies me</p></td>
    </tr>
</table>

  <h3>:question: What we did?</h3>
  <p align="justify">In the 2nd sprint we made changes in the new samples registration interface so that the user can send the images and verify it's analysis results generated with the model we trained in the 1st sprint.
  </p>

  <h3>:grey_question: Why?</h3>
  <p align="justify">Viewing the analysis result before confirming your record is highly important to ensure data integrity, as it allows the user to decide whether the analysis was successful or not.</p>
  
<h2>:running_woman: ehSoja running :computer::computer_mouse:</h2>
<p align="justify">Below we have the mock-ups created for the 2nd sprint and a GIF exemplifying the flow of use inside the eSoja app.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Mockups/after/registro.png" height="600px"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Mockups/after/confirmacao.png" height="600px"/>
</p>
<p align="justify">For this sprint we integrated the application with the dispatch of the images and the recognition of the pods in the images. You can click on the preview option to quickly analyze the chosen image, or finish importing all the images. Then in the last step the request is made automatically and all the images are analyzed at once.

Compared to the last sprint, we started training a model that does the segmentation of the pods, and not just their location in the image.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_2/ehSoja-Sprint-2.gif" height="600px"/>
</p>
<p align="justify">We have made several attempts to improve the IoU, Intersection over Union, which is calculated from the division between the detection masks and the masks annotated by us. Finally, we obtained a percentage of 20% similarity between the segmentations.

Among one of the used techniques, we performed data augmentation to pass more examples to our model, but we obtained small advances. We will review all annotations made by us to verify they are correct, as well as ask to our teachers about other techniques.</p>
  
<h3><i>:crossed_flags: Definition Of Ready</i></h3>
<p align="justify">The following artifacts were generated so that the team could start the development stage:</p>

- Sprint's epics
<table>
    <tr>
        <td width="1000px"><p align="center">Create/change the old plant's registration interface to give to the user access to the new functionalities</p></td>
    </tr>
    <tr>
        <td><p align="center">Create an interface that allows the user to visualize the image analysis result</p></td>
    </tr>
</table>

- User stories
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">I, as an user, have access to the new interface to register a plant</p></td>
        <td><p align="justify">With the access to the new interface, I can register a plant with the new requested data</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can take a new photo by the application to register a plant</p></td>
        <td><p align="justify">Taking a photo without have to photograph it previously make the steps be faster</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can choose a photo from my gallery to register a plant</p></td>
        <td><p align="justify">If I already has the photo of the plant that I want to register, choosing it from my gallery will speed up the steps</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, submit the plant’s photo to be analyzed</p></td>
        <td><p align="justify">Submitting the plant's photo be analyzed will allow me to know if I submit a good photo</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, receive the analyzed image with the identified elements marked on it
to check if the identification is satisfactory</p></td>
        <td><p align="justify">Receiving the analyzed photo will allow me to check if the submitted photo was good and ensure that I will only register if the analysis satisfies me</p></td>
    </tr>
</table>

- Mock-ups
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Mockups/after/registro.png" height="600px"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Mockups/after/confirmacao.png" height="600px"/>
</p>

<h3><i>:crossed_flags: Definition Of Done :white_check_mark:</i></h3>
<p align="justify">Following the backlog gathered for the delivery of the sprint's valuable product, the artifacts generated for the costumer were:</p>

- [Source code](https://github.com/barbaraport/softtelie-ehsoja/tree/main/src)

- New functionality in the application: The user can now view the image analysis result to be submitted for the registration of a new sample.
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Mockups/after/registro.png"/>
</p>

<h2 align="center"><i>Burndown</i> :date::chart_with_downwards_trend:</h3>
<p align="justify">Taking a look at the burndown of the 2nd sprint, it was possible to see that most of the time we were behind schedule. The detection of the sent image was successfully implemented and without any delays, but its integration with the application was difficult, since the application code is complex. We tried our best to get a better result at the end of the sprint and in the last few days we dedicated ourselves to carrying out all our documentation.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Burndown/sprint_2.png"/>
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
