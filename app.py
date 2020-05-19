from flask import Flask, render_template, redirect, request
import RapGenerationML


app = Flask(__name__)

@app.route('/')
def hello(): 
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def home():
    if request.method=="POST":
        f= request.files['userfile']
        path="./static/{}".format(f.filename)
        f.save(path)
        line= request.form['usertext']
        # print(line)
        rap=RapGenerationML.rapthis(path,line)
        # print(rap)
        
    return render_template("index.html", raps=rap)

if __name__ == '__main__':

    app.run(debug = True) 