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
    product=Product.query.all()
    return render_template("productlist.html",product=product)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.form:
        new_product=Product(
            url=request.form['url'],
            alt=request.form['alt'],
            name=request.form['name'],
            price=request.form['price'],
            size=request.form['size'],
            material=request.form['material'],
            type=request.form['type'],
            caution=request.form['caution'],
            delivery=request.form['delivery'],
            description=request.form['description']
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('productlist'))
    print(request.form)
    return render_template("add.html")


@app.route("/edit")
def edit():
    return render_template("edit.html")



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
