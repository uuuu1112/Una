from flask import Flask,redirect,url_for,render_template,url_for,request

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

@app.route("/productlist")
def productlist():
    return render_template("productlist.html")

@app.route("/add",methods=['GET','POST'])
def add():
    return render_template("add.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/test")
def test():
    return render_template("test.html")


if __name__=="__main__":
    app.run(debug=True)