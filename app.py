from flask import redirect, url_for, render_template, url_for, request
from models import db, app, Product


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
    product=Product.query.all
    return render_template("productlist.html",product=product)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.form:
        print(request.form)
        new_product = Product(name=request.form['name'], price=request.form['price'],
                              size=request.form['size'], photo=request.form['photo'],
                              category=request.form['category'], material=request.form['material'],
                              caution=request.form['caution'], delivery=request.form['delivery'],
                              alt=request.form['alt'])
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('productlist'))
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
