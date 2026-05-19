from fastapi import FastAPI
from db import Base, engine , SessionLocal
import models
from models import Product, Category
from schema import CreateCategory, UpdateCategory, CreateProduct, UpdateProduct


models.Base.metadata.create_all(bind= engine)
app = FastAPI()




@app.get("/")
def show_all_products_and_their_categories():
    db = SessionLocal()
    products = db.query(Product).all()
    print("products are ", products)
    return products
    


# get all the categories with the pagination of 10 categories per page default
@app.get('/api/categories')
def get_all_categories(page:int  = 1):
    db = SessionLocal()
    LIMIT = 10   
    OFFSET = (page - 1) * 10
    categories = db.query(Category).offset(OFFSET).limit(LIMIT).all()
    if categories:
        print("fetched all the categories ", categories)
        return {
            "categories": categories, 
            "page": page,
            "limit": LIMIT
        }
    else:
        return {"message": "No categories found"}


#category by id 
@app.get('/api/categories/{category_id}')
def get_category_by_id(category_id: int):
    db = SessionLocal()
    category = db.query(Category).filter(Category.id == category_id).first()
    
   
    if category:
        print("fetched category ", category)
        return {
            "category": category,
            }
    else:
        return {"message": "Category not found with this id"}


@app.post('/api/category')
def add_category(category:CreateCategory):
    db = SessionLocal()
    new_category = Category(category_name = category.category_name)
    db.add(new_category)   
    db.commit()
    db.refresh(new_category)
    print("added new category ", new_category)
    return new_category


@app.put('/api/category/{category_id}')
def update_category(category:UpdateCategory, category_id: int):
    db = SessionLocal()
    category_update = db.query(Category).filter(Category.id == category_id).first()
    if category_update:
        category_update.category_name = category.category_name
        db.commit()
        db.refresh(category_update)
        print("updated category ", category_update)
        return category_update
    else:
        return {"message": "Category not found with this id to update"}


@app.delete('/api/category/{category_id}')
def delete_category(category_id: int):
    db = SessionLocal()
    category_delete = db.query(Category).filter(Category.id == category_id).first()
    if category_delete:
        db.delete(category_delete)
        db.commit()
        print("deleted category ", category_delete)
        return {"message": "Category deleted successfully"}
    else:
        return {"message": "Category not found with this id to delete"}




#get all the products with the paginaition of 10 products per page default
@app.get('/api/products')
def get_all_products(page: int = 1):
    db = SessionLocal()
    products = db.query(Product).all()
    LIMIT  = 10
    OFFSET = (page - 1) * LIMIT
    
    products = db.query(Product).offset(OFFSET).limit(LIMIT).all()
    return {
        "products": products,
        "page": page,
         "limit":LIMIT,
    }


#get single  products by id 
@app.get('/api/products/{product_id}')
def get_product_by_id(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    associate_category_details = db.query(Category).filter(Category.id == product.category_id).first() if product else None
    if associate_category_details:
        print("fetched associated category details ", associate_category_details)
    if product:
        print("fetched product ", product)
        return {
            "product": product,
            "associated_category_details": associate_category_details
        }
    else:
        return {"message": "Product not found with this id"}






@app.post('/api/product')
def add_product(product: CreateProduct):
    db = SessionLocal()
    new_product = Product(product_name = product.product_name, category_id = product.category_id)
    db.add(new_product)   
    db.commit()
    db.refresh(new_product)
    print("added new product ", new_product)
    return new_product


@app.put('/api/product/{product_id}')
def update_product(product : UpdateProduct, product_id: int):
    db = SessionLocal()
    product_update = db.query(Product).filter(Product.id == product_id).first()
    if product_update:
        product_update.product_name = product.product_name
        product_update.category_id = product.category_id
        db.commit()
        db.refresh(product_update)
        print("updated product ", product_update)
        return product_update
    else:
        return {"message": "Product not found with this id to update"}
    


@app.delete('/api/product/{product_id}')
def delete_product(product_id: int):
    db = SessionLocal()
    product_delete = db.query(Product).filter(Product.id == product_id).first()
    if product_delete:
        db.delete(product_delete)
        db.commit()
        print("deleted product ", product_delete)
        return {"message": "Product deleted successfully"}
    else:
        return {"message": "Product not found with this id to delete"}