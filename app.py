from flask import Flask,redirect,url_for,render_template,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/category")
def category():
    return render_template("category.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/test")
def test():
    return render_template("test.html")


if __name__=="__main__":
    app.run(debug=True)