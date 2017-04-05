# Smiley Face Discriminator

Using [Clarifai's api](https://www.clarifai.com/) we created a custom model that discriminates emotional state of a drawn "smiley face". This was part of R/GA / Somatic Hackday March 2017. To demonstrate the model we have a slack bot that listens for images uploads and then adds an emoticon reaction based on prediction of whether the drawing is a smiley face or not. 

## Clarifai setup

We had to create an application to represent the model. We noticed that the application had to be recreated everytime we trained a new model, because it expected unique images. Perhaps if we made the image paths unique during training step we could have avoided this.

Clarifai uses a base image model which is what gives the service its magic. You can use a very small training data set to make custom models that work very well.

## Training images

We scanned about 25 images to be used in positive training.

![Smiley](./smileys_1/smileys_0000.jpg)

About 10 images for negatives.

![Not Smiley](./not_smileys_1/0001.jpg)

We saved a small set of imagse each from the Positives and Negatives to test after training.

## Predictions

We were able to get a decent prediction after this very small training set.

*88% chance of "Smiley" for the postive test
*6% chance of "Smiley" for the negative test

## Slack bot 

To make the model accessible we created a bot. This simply adds a reaction to uploaded images. 

![Slack bot](./img/slack.png)


