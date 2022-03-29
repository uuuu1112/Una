from flask import redirect, url_for, render_template, url_for, request
from models import db, app, Product


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/category")
def category():
    product=Product.query.all()
    return render_template("category.html",product=product)


@app.route("/product/<id>")
def product(id):
    product=Product.query.get(id)
    return render_template("product.html",product=product)


@app.route("/productlist")
def productlist():
    product=Product.query.all()
    return render_template("productlist.html",product=product)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.form:
        new_product=Product(
            url=request.form['url'],
            name=request.form['name'],
            detail=request.form['detail']
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('productlist'))
    print(request.form)
    return render_template("add.html")


@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/test")
def test():
    return render_template("test.html")



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
