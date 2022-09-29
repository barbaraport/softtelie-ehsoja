
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
ehSoja is a new module for recognizing soybean plants through the <a href="https://github.com/cluster-8/esoja-mobile">eSoja</a> app! eSoja is a mobile application for the agricultors, in specific, soy farmers. eSoja provides its users with features that help them in monitoring, controlling and obtaining forecasts about their planting and harvesting. Our eSoja extension, ehSoja, enhances the native functions of the application and provides it with an innovation. Currently, the user needs to manually enter the number of pods within a plant so that the aplication can estimate the harvest data for them. Therefore, we developed the <i>upload</i> of a soybean plant image so that informations like the amount of pods and grains per pod can be deduced through an analysis of the image. This functionality guarantees agility and versatility to the user, who will no longer need to make an effort to obtain an estimate of his harvest.
</p>
  
  <h2 align="center">:rainbow::spiral_calendar: First delivery :stars:</h2>
  <h3>:question: O que fizemos?</h3>
  <p align="justify">In the 1st <i>sprint</i> we decided to start the project by taking a first step into the identification of soybean plants and its pods from the sample images we received.
  </p>
  <p align="center">
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/Backlog_Sprint1.png" width="400px"/>
    <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Backlog/UserStories_Sprint01.png" height="210px"/>
  </p>
  <h3>:grey_question: Why?</h3>
  <p align="justify">Recognizing the plant and its pods is requires time and a good refinement of the model the most. Therefore, we deliver this version in order to show our potential and receive <i>feedback</i> faster so that we have better chances of getting a model close to perfection.</p>
  
<h2>:running_woman: ehSoja running :computer::computer_mouse:</h2>
<p align="justify">Down below we have the images obtained from training our model to detect plants and its pods. There are a few cases where the shadows, parts of plant roots and leaves were recognized as pods. That being said, we need to adjust our model looking forward to solve these issues.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/10test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/11test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/14val_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/15test_result_cropped.png"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_1/15val_result_cropped.png"/>
</p>
  
<h3><i>:crossed_flags: Definition Of Ready</i></h3>
<p align="justify">In order to start the development of each requirement, it must be well-comprehended and subdivided into several tasks for the developers. That being said, each of the small tasks generated receive a description of what must be done and its priority. Tasks that are more difficult may block the execution of another task, so they usually receive top priority. Finally, developers can proactively initiate a task.</p>

<h3><i>:crossed_flags: Definition Of Done :white_check_mark:</i></h3>
<p align="justify">For each task to be considered done, it is necessary to review the code in order to avoid conflicts, add improvements and verify if it meets its expectations. After the first evaluation, the reviewer will run the system in order to check if there are bugs or other issues that may have arisen after the implementation. The code will go into production only after this verification is complete.</p>

<h2 align="center"><i>Burndown</i> :date::chart_with_downwards_trend:</h3>
<p align="justify">During our sprint we had several technical difficulties as artificial intelligence is a new subject for us to work with. Even so, we made an effort and kept our focus, as we are committed to delivering value to our customers.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Burndown/sprint_1.png"/>
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
