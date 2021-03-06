from typing import NewType
from flask import redirect, url_for, render_template, url_for, request
from models import db, app, Product
import info

# 主頁
@app.route("/") 
def home():
    onseason=Product.query.filter_by(type="mother").limit(4).all()
    return render_template(
        "index.html",
        sideBarDetail=info.SideBar.detail,
        categoryAll=info.Category.all,
        categoryinIndex=info.Category.inIndex,
        categoryDetail=info.Category.detail,
        homePage=info.HomePage,
        onseason=onseason,
        )
# 聯絡我們
@app.route("/contact") 
def contact():
    return render_template(
        "contact.html",
        sideBarDetail=info.SideBar.detail,
        categoryAll=info.Category.all,
        precautionItems=info.Precaution.items
        )

# 分類頁面
@app.route("/category")
def category():
    type=request.args.get("type","")
    onseason=request.args.get("onseason","")
    if type != "":
        products=Product.query.filter_by(type=type).order_by(Product.price).all()
    if onseason !="":
        products=Product.query.filter_by(onseason=onseason).all()
    if type=="" and onseason=="":
        products=Product.query.order_by(Product.type).all()
    # else:
    #     print("3",type)
    #     products=Product.query.order_by(Product.type).all()
    return render_template(
        "category.html",
        type=type,
        products=products,
        sideBarDetail=info.SideBar.detail,
        categoryinIndex=info.Category.inIndex,
        categoryAll=info.Category.all,
        categoryDetail=info.Category.detail,
        )
        
# 商品頁面
@app.route("/product/<id>")
def product(id):
    product=Product.query.get(id)
    return render_template(
        "product.html",
        product=product,
        sideBarDetail=info.SideBar.detail,
        categoryDetail=info.Category.detail,
        categoryAll=info.Category.all
        )

# 可編輯分類頁面後台
@app.route("/productlist")
def productlist():
    product=Product.query.all()
    return render_template(
        "productlist.html",
        product=product,
        categoryDetail=info.Category.detail,
        categoryOnSeason=info.Category.onseason,
        )

# 增加商品頁面
@app.route("/add",methods=["GET","POST"])
def add():
    if request.form:
        categoryDetail=info.Category.detail
        new_product=Product(
            url=request.form['url'],
            name=request.form['name'],
            detail=request.form['detail'],
            type=categoryDetail[request.form['detail']]["type"],
            price=categoryDetail[request.form['detail']]["price"],
            onseason=request.form["onseason"],
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('productlist'))
    return render_template(
        "add.html",
        categoryAll=info.Category.all,
        categoryDetail=info.Category.detail,
        categoryPureType=info.Category.pureType,
        )

# 編輯商品頁面
@app.route("/edit/<id>",methods=['GET','POST'])
def edit(id):
    categoryDetail=info.Category.detail

    product=Product.query.get(id)
    if request.form:
        product.name=request.form['name']
        product.url=request.form['url']
        product.detail=request.form['detail']
        product.type=categoryDetail[request.form['detail']]["type"]
        product.price=categoryDetail[request.form['detail']]["price"]
        product.onseason=request.form['onseason']
        db.session.commit()
        return redirect(url_for('productlist'))
    return render_template(
        "edit.html",
        product=product,
        categoryDetail=categoryDetail,
        categoryAll=info.Category.all,
        categoryPureType=info.Category.pureType,
        )

# 刪除商品
@app.route("/delete/<id>")
def delete(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("productlist"))

@app.route("/test")
def test():
    return render_template(
        "test.html",
        )

@app.route("/test2")
def test2():
    return render_template(
        "test2.html",
        categoryAll=info.Category.all,
        categoryDetail=info.Category.detail,
        categoryPureType=info.Category.pureType,
    )



if __name__ == "__main__":
    db.create_all()
    # app.run(host="0.0.0.0",port=5000)
    app.run(debug=True)
