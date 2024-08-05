from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class ProductRepository():
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, product: schemas.Product):
        db_product = models.Product(name = product.name,)
    
    def list(self):
        pass
    
    def obtain(self):
        pass
    
    def remove(self):
        pass