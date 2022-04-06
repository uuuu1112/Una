from flask import redirect, url_for, render_template, url_for, request
from models import db, app, Product
import detail



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/category/<type>")
def category(type):
    products=Product.query.filter_by(type=type).all()
    return render_template("category.html",products=products)


@app.route("/product/<id>")
def product(id):
    product=Product.query.get(id)
    global detail
    new_detail=detail.Detail()
    return render_template("product.html",product=product,detail=new_detail)


@app.route("/productlist")
def productlist():
    product=Product.query.all()
    return render_template("productlist.html",product=product)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.form:
        global detail
        new_detail=detail.Detail()
        new_product=Product(
            url=request.form['url'],
            name=request.form['name'],
            detail=request.form['detail'],
            type=new_detail.type[request.form['detail']]
        )
        print(new_product.type)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('productlist'))
    print(request.form)
    return render_template("add.html")


@app.route("/edit/<id>",methods=['GET','POST'])
def edit(id):
    global detail
    new_detail=detail.Detail()
    product=Product.query.get(id)
    if request.form:
        product.name=request.form['name']
        product.url=request.form['url']
        product.detail=request.form['detail']
        product.type=new_detail.type[request.form['detail']]
        db.session.commit()
        return redirect(url_for('productlist'))
    return render_template("edit.html",product=product)

@app.route("/delete/<id>")
def delete(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("productlist"))

@app.route("/test")
def test():
    # global detail
    # detail=detail.Detail()
    return render_template("test.html",detail=detail)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
