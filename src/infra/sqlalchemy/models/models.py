from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)