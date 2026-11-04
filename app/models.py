from app.database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default="operador")  # Ex: operador, admin


class MaterialCategory(Base):
    __tablename__ = "material_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)  # Ex: Papelão Ondulado
    price_per_kg = Column(Float, nullable=False)


class ScaleLog(Base):
    __tablename__ = "scale_logs"

    id = Column(Integer, primary_key=True, index=True)
    coop_name = Column(String, nullable=False)
    material_category = Column(String, nullable=False)
    weight_kg = Column(Float, nullable=False)
    estimated_value = Column(Float, nullable=False)
    operator_cpf = Column(String, nullable=False)