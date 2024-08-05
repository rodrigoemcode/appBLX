from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class ProductRepository():
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, product: schemas.Product):
        db_product = models.Product(name = product.name,
                                    detail=product.detalhes,
                                    price = product.price,
                                    status = product.status)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    def list(self):
        products = self.db.query(models.Product).all()
        return db_product
    
    def obtain(self):
        pass
    
    def remove(self):
        pass