# Coconut-Grade-Classification-using-CNN

The main objective here is to build a "Dehusked coconut classifier" which can classify the images taken of coconut into different grades according to their quality. <br />
Coconuts used for exporting (1st grade), food (grade 2) and for oil press(grade 3).<br />
The images were collected from different farms to increase variety. <br />
Grade 3 images are less, it is difficult to get as they aren't given importance by the farmers, yet managed to get. <br />
IMAGES AT THE BEGINNING:<br />
  Grade 1 = 250<br />
  Grade 2 = 250<br />
  Grade 3 = 250<br />
  
We would need more images for Model to train better for which we Augument them and add it to Dataset, Augumenting is basically introducing noise, such as flipping, blurring the images for it to predict properly despite the changes.
<br />
As we add them to our dataset, number of images increase
IMAGES AT THE BEGINNING:<br />
  Grade 1 = 1000<br />
  Grade 2 = 1000<br />
  Grade 3 = 832<br />
  
  Our CNN model architecture consists of 5 convulutional and 5 pooling layers, output layer has 3 nodes. <br />
  once we fit the model and train them, the model is ready! <br />
  Kindly look into my Notebook, open to suggestions and advices. <br />
  Model's accuracy is about 86.63%

  
 
