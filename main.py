from flask import Flask,render_template,request



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")







if __name__=="__main__":
    app.run(debug=True)

