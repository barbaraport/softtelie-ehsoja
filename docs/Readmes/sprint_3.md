
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
<table>
    <tr>
        <td width="1000px"><p align="center">Improve the pods recognition model</p></td>
    </tr>
    <tr>
        <td><p align="center">Perform the count of how many pods has been identified</p></td>
    <tr>
        <td><p align="center">Update the database with the extracted information from the image analysis</p></td>
    </tr>
    <tr>
        <td><p align="center">Review the statistics interface to show to the user the amount of identified pods</p></td>
    </tr>
</table>

<h2 align="center">:astronaut: User Stories :label:</h2>
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">I, as an user, submit a request to register new plants samples</p></td>
        <td><p align="justify">With the register of new samples, I can update the informations of my plot</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can visualize, in the page of the plot's statistics, the registered samples</p></td>
        <td><p align="justify">Visualize the registered samples ensures to me that the register was well succeeded</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can visualize, in the details of the samples in the statistics page, the amount of identified pods in the image</p></td>
        <td><p align="justify">Knowing how many pods has been identified by the analysis, I can take later decisions based on this data</p></td>
    </tr>
</table>

  <h3>:question: What we did?</h3>
  <p align="justify">In the 3rd sprint, we updated the database model to store the recognized data from the plot's new samples, changed the page of statistics of a plot to show this new data and performs adjusts in the detection model in a way that it can better detect the pods in an image.
  </p>

  <h3>:grey_question: Why?</h3>
  <p align="justify">Updating the database model and changing the statistics page to show the new information grants to the user the possibility to know exactly what informations the detection model has extracted from the image and the adjusts in the model was done to make it perform a better extraction of the information within the given image.</p>
  
<h2>:running_woman: ehSoja running :computer::computer_mouse:</h2>
<p align="justify">For this sprint we integrated the application with the dispatch of the images and the counting of the recognized pods in the images. You can click on the preview option to quickly analyze the chosen image or finish importing all the images. After the pods of all images have been counted, the user is redirected to the statistics pages, where is shown the amount of pods in each sample.</p>
<p align="justify">In the GIF bellow, it's shown the registration of a new plant sample for the plot with the analysis of the image. After the registration, the user access the statistics page and it displays the informations extracted from the analysis, in specially the amount of pods detected by the detection model.</p>

<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_3/ehSoja-Sprint-3.gif" height="600px"/>
</p>
<p align="justify">Below are more examples of how our trained model performed after our changes. We can notice that some objects that are not even close to being pods are also considered to be pods, and we are already researching how to improve this flaw. We are considering the hypothesis that this detail is decreasing our IoU.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_3/example1.png" height="400px"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_3/example2.png" height="400px"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_3/example3.png" height="400px"/>
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_3/example4.png" height="400px"/>
</p>

<p align="justify">We have made several attempts to improve the IoU, Intersection over Union, which is calculated from the division between the detection masks and the masks annotated by us. Finally, we obtained a percentage of 44% similarity between the the ground-truth bounding boxes and the predicted bounding boxes. The successfull attempts were:</p>
<ul>
    <li>Choosing better images for model training and validation;</li>
    <li>Training with the <b>Learning Rate</b> of 0.0001;</li>
    <li>Changing some Mask RCNN's hyper parameters:</li>
    <ul>
        <li><b>BACKBONE</b> changed from Resnet101 to Resnet50;</li>
        <li><b>BATCH_SIZE</b> changed to 32. The default value is the GPU_COUNT times the IMAGES_PER_GPU;</li>
        <li><b>DETECTION_MIN_CONFIDENCE</b> changed from 0.7 to 0.6;</li>
        <li><b>IMAGE_RESIZE_MODE</b> set to none, because we already make this step before the training;</li>
        <li><b>IMAGE_MAX_DIM</b> and <b>IMAGE_MIN_DIM</b> set to 1024;</li>
        <li><b>DETECTION_NMS_THRESHOLD</b> set to 0.1 to increase the quantity of objects that can be a pod;</li>
        <li><b>RPN_ANCHOR_SCALES</b> set to (8, 16, 32, 64, 128), so that Mask R-CNN can predict smallest objects;</li>
        <li><b>RPN_NMS_THRESHOLD</b> set to 0.1 to increase the quantity of proposals of what can be a pod;</li>
    </ul>
    <li>Applying data augmentation (flip, crop, rotate, translation...);</li>
    <li>Improving the amount of images for calculate the IoU, and</li>
    <li>Changing the <b>IoU threshold</b> to 0.1.</li>
</ul>
  
<h3><i>:crossed_flags: Definition Of Ready</i></h3>
<p align="justify">The following artifacts were generated so that the team could start the development stage:</p>

- Sprint's epics
<table>
    <tr>
        <td width="1000px"><p align="center">Improve the pods recognition model</p></td>
    </tr>
    <tr>
        <td><p align="center">Perform the count of how many pods has been identified</p></td>
    <tr>
        <td><p align="center">Update the database with the extracted information from the image analysis</p></td>
    </tr>
    <tr>
        <td><p align="center">Review the statistics interface to show to the user the amount of identified pods</p></td>
    </tr>
</table>

- User stories
<table>
    <thead>
        <th>Story :label:</th>
        <th>Why :star:</th>
    </thead>
    <tr>
        <td><p align="justify">I, as an user, submit a request to register new plants samples</p></td>
        <td><p align="justify">With the register of new samples, I can update the informations of my plot</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can visualize, in the page of the plot's statistics, the registered samples</p></td>
        <td><p align="justify">Visualize the registered samples ensures to me that the register was well succeeded</p></td>
    </tr>
    <tr>
        <td><p align="justify">I, as an user, can visualize, in the details of the samples in the statistics page, the amount of identified pods in the image</p></td>
        <td><p align="justify">Knowing how many pods has been identified by the analysis, I can take later decisions based on that</p></td>
    </tr>
</table>

- Mock-ups
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Mockups/sprint_3/newStatisticsPage.jpeg" height="600px"/>
</p>

- New database model: The table with the reddish color indicates the modified table in the new database model.
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Modelo%20de%20dados/modelo_sprint_3.png" height="600px"/>
</p>

<h3><i>:crossed_flags: Definition Of Done :white_check_mark:</i></h3>
<p align="justify">Following the backlog gathered for the delivery of the sprint's valuable product, the artifacts generated for the costumer were:</p>

- [Source code](https://github.com/barbaraport/softtelie-ehsoja/tree/main/src)

- New functionality in the application: The user can now view in the plot's statistics page the extracted information of the image.
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/MVPs/sprint_3/ehSoja-Sprint-3.gif" height="600px"/>
</p>

- The pod's recognition model was improved to recognize the pods in the given image.

- The database model was updated to reflect the new data that is generated when registering a sample.

<h2 align="center"><i>Burndown</i> :date::chart_with_downwards_trend:</h3>
<p align="justify">Looking at the burndown of the sprint, it's possible to see that the team was ahead of the time with the completion of the tasks, which results in more time to be afford on the improvement of the recognition model.</p>
<p align="center">
  <img src="https://github.com/barbaraport/softtelie-ehsoja/blob/main/docs/Burndown/sprint_3.png"/>
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
