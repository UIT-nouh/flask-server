from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import os
application = Flask(__name__)

CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
application.config['UPLOAD_FOLDER'] = "static"

@application.route("/", methods = ['GET','POST'])
def hello():
  if request.method == "POST":
    image = request.files['file']
    if image:
      path_to_save = os.path.join(application.config['UPLOAD_FOLDER'], image.filename)
      image.save(path_to_save)
      return render_template("index.html", link = request.url + path_to_save)
  else:
    return render_template("index.html", link = '')


if __name__ == "__main__":
  application.run(debug = True)