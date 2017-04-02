from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
import json

print "** running training **"

app_id = os.environ["clarifai_app_id"]

app_secret = os.environ["clarifai_app_secret"]

app = ClarifaiApp(app_id=app_id,
    app_secret=app_secret)


# import a few labeld images
model_id = "smilies"

images = []
print ("loading positives...")
for i in range(22):
  url = "./smileys_1/smileys_"+ str(i).zfill(4)+".jpg"
  print (url)
  img = ClImage(filename=url, concepts=["smiley"])
  images.append(img)

print ("loading negatives...")
for i in range(10):
  url = "./not_smileys_1/"+ str(i+1).zfill(4)+".jpg"

  print (url)
  img = ClImage(filename=url, not_concepts=["smiley"])
  images.append(img)


app.inputs.bulk_create_images(images)

model = app.models.create(model_id=model_id, concepts=["smiley"])
#
model = model.train()
# #model = get(model_id)
#
# predict with samples
print "**smiley test**"
#output = model.predict_by_filename("./smileys_1/smileys_0023.jpg")
#print output["u'outputs'"]["u'data'"]["u'concepts"]
print model.predict_by_filename("./smileys_1/smileys_0023.jpg")

print "**not smiley test**"
#output = model.predict_by_filename("./not_smileys_1/0010.jpg")
#print output["u'outputs'"]["u'data'"]["u'concepts"]
print model.predict_by_filename("./not_smileys_1/0010.jpg")
