from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
import json

app_id = os.environ["clarifai_app_id"]

app_secret = os.environ["clarifai_app_secret"]

app = ClarifaiApp(app_id=app_id,
    app_secret=app_secret)

model_id = "smilies"

model = app.models.get(model_id)

print "**smiley test**"
output = model.predict_by_filename("./smileys_1/smileys_0023.jpg")
print output

print "**not smiley test**"
output = model.predict_by_filename("./not_smileys_1/0010.jpg")
print output
