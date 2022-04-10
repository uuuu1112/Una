from typing import NewType
from flask import redirect, url_for, render_template, url_for, request
from models import db, app, Product
import info

@app.route("/")
def home():
    productDetail=info.IndexItem.productDetail
    return render_template(
        "index.html",
        productDetail=productDetail)


@app.route("/category/<type>")
def category(type):
    products=Product.query.filter_by(type=type).all()
    productDetail=info.IndexItem.productDetail
    newType=info.IndexItem.newType
    return render_template(
        "category.html",
        products=products,
        productDetail=productDetail,
        newType=newType)


@app.route("/product/<id>")
def product(id):
    product=Product.query.get(id)
    new_detail=info.Detail()
    return render_template("product.html",product=product,detail=new_detail)


@app.route("/productlist")
def productlist():
    product=Product.query.all()
    return render_template("productlist.html",product=product)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.form:
        new_detail=info.Detail()
        new_product=Product(
            url=request.form['url'],
            name=request.form['name'],
            detail=request.form['detail'],
            type=new_detail.itemCategory[request.form['detail']]["type"],
            price=new_detail.itemCategory[request.form['detail']]["price"],
            onseason=request.form["onseason"],
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('productlist'))
    return render_template("add.html")


@app.route("/edit/<id>",methods=['GET','POST'])
def edit(id):
    new_detail=info.Detail()
    product=Product.query.get(id)
    if request.form:
        product.name=request.form['name']
        product.url=request.form['url']
        product.detail=request.form['detail']
        product.type=new_detail.itemCategory[request.form['detail']]["type"]
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
    return render_template("test.html",detail=info)



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
