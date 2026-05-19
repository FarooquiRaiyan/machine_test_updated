from pydantic import BaseModel



class CreateCategory(BaseModel):
    category_name : str
    


class UpdateCategory(BaseModel):
    category_name : str
    id : int
    

class CreateProduct(BaseModel):
    product_name : str
    category_id : int
    

class UpdateProduct(BaseModel):
    id: int
    product_name : str
    category_id : int