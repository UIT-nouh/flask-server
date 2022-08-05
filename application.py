from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/", methods = ['GET','POST'])
def hello():
  if request.method == "POST":
    a = int(request.form['so_phong'])
    print(a)
    gia = a*60000000+ a*a*1000000 + a*1.24135 + 0.9724
    return render_template("index.html", g = 'gia can de xay tro la ' + str(gia))
  else:
    return render_template("index.html", g = '')


if __name__ == "__main__":
  application.run(debug = True)