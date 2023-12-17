from flask import Flask, render_template, request

#import tensorflow as tf
import numpy as np



from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from tensorflow.keras.models import load_model

import joblib

model = load_model('tb_model.h5')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "deployment/images/" + imagefile.filename
    imagefile.save(image_path)

    image_size = 200
    image = load_img(image_path, target_size=(image_size, image_size))
    



    
    image = img_to_array(image)



    # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # image = preprocess_input(image)
    image = image.reshape(1,image_size,image_size,3)
    p = model.predict(image)
    p = np.argmax(p,axis=1)[0]
    print("P je jednanko ", p)
    if p==0:
        classification ='The model predicts that these lungs are NOT infected with tuberculosis'
    else:
        classification ='The model predicts that these lungs ARE infected with tuberculosis'

    print(classification)

    return render_template('index.html', prediction=classification)



if __name__ == '__main__':
    app.run(port=3000, debug=True)